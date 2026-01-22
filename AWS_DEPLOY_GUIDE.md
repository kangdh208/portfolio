# AWS 배포 가이드

Django 포트폴리오를 AWS에 배포하는 방법입니다.

## 배포 옵션

### 옵션 1: AWS Elastic Beanstalk (추천 - 가장 쉬움)

#### 1. 사전 준비
```bash
# AWS CLI 설치
pip install awscli
aws configure  # AWS Access Key 설정

# EB CLI 설치
pip install awsebcli
```

#### 2. Elastic Beanstalk 초기화
```bash
cd portfolio
eb init -p python-3.11 portfolio-app --region ap-northeast-2
```

#### 3. 환경 생성 및 배포
```bash
eb create portfolio-env
```

#### 4. 환경변수 설정
```bash
eb setenv DJANGO_SECRET_KEY='your-secret-key-here' DEBUG=False ALLOWED_HOSTS='.elasticbeanstalk.com'
```

#### 5. 배포
```bash
eb deploy
```

#### 6. 웹사이트 열기
```bash
eb open
```

---

### 옵션 2: AWS EC2 (더 많은 제어권)

#### 1. EC2 인스턴스 생성
- AWS 콘솔 → EC2 → 인스턴스 시작
- Ubuntu 22.04 LTS 선택
- t2.micro (프리티어) 선택
- 보안 그룹: 22(SSH), 80(HTTP), 443(HTTPS) 포트 열기

#### 2. EC2 접속
```bash
ssh -i your-key.pem ubuntu@your-ec2-ip
```

#### 3. 서버 설정
```bash
# 시스템 업데이트
sudo apt update && sudo apt upgrade -y

# Python 및 필요 패키지 설치
sudo apt install python3-pip python3-venv nginx -y

# 프로젝트 디렉토리 생성
mkdir -p ~/portfolio
cd ~/portfolio

# 가상환경 생성
python3 -m venv venv
source venv/bin/activate

# 프로젝트 파일 업로드 (로컬에서)
# scp -i your-key.pem -r portfolio/* ubuntu@your-ec2-ip:~/portfolio/

# 의존성 설치
pip install -r requirements.txt

# Static 파일 수집
python manage.py collectstatic --noinput
```

#### 4. Gunicorn 설정
```bash
# Gunicorn 서비스 파일 생성
sudo nano /etc/systemd/system/gunicorn.service
```

내용:
```ini
[Unit]
Description=gunicorn daemon for portfolio
After=network.target

[Service]
User=ubuntu
Group=www-data
WorkingDirectory=/home/ubuntu/portfolio
Environment="DJANGO_SECRET_KEY=your-secret-key"
Environment="DEBUG=False"
Environment="ALLOWED_HOSTS=your-domain.com,your-ec2-ip"
ExecStart=/home/ubuntu/portfolio/venv/bin/gunicorn --workers 3 --bind unix:/home/ubuntu/portfolio/portfolio.sock portfolio.wsgi:application

[Install]
WantedBy=multi-user.target
```

```bash
# Gunicorn 시작
sudo systemctl start gunicorn
sudo systemctl enable gunicorn
```

#### 5. Nginx 설정
```bash
sudo nano /etc/nginx/sites-available/portfolio
```

내용:
```nginx
server {
    listen 80;
    server_name your-domain.com your-ec2-ip;

    location /static/ {
        alias /home/ubuntu/portfolio/staticfiles/;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/home/ubuntu/portfolio/portfolio.sock;
    }
}
```

```bash
# Nginx 설정 활성화
sudo ln -s /etc/nginx/sites-available/portfolio /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx
```

---

### 옵션 3: AWS Lightsail (저렴하고 간단)

#### 1. Lightsail 인스턴스 생성
- AWS Lightsail 콘솔 접속
- 인스턴스 생성 → Linux/Unix → Ubuntu 22.04
- $3.50/월 플랜 선택

#### 2. 이후 과정은 EC2와 동일

---

## 공통 작업

### Static 파일 수집
배포 전 반드시 실행:
```bash
python manage.py collectstatic --noinput
```

### 프로필 이미지 추가
`static/img/my_image.jpg`에 증명사진을 넣어주세요.

### 환경변수 설정
프로덕션에서 필수로 설정해야 할 환경변수:
- `DJANGO_SECRET_KEY`: 고유한 비밀 키 (최소 50자 이상 랜덤 문자열)
- `DEBUG`: `False`
- `ALLOWED_HOSTS`: 도메인 또는 IP 주소

### SECRET_KEY 생성 방법
```python
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
```

---

## 도메인 연결 (선택사항)

### Route 53 사용
1. Route 53에서 호스팅 영역 생성
2. A 레코드 추가 → EC2/Lightsail IP 연결
3. ALLOWED_HOSTS에 도메인 추가

### SSL 인증서 (HTTPS)
```bash
# Certbot 설치
sudo apt install certbot python3-certbot-nginx -y

# SSL 인증서 발급
sudo certbot --nginx -d your-domain.com
```

---

## 문제 해결

### 502 Bad Gateway
```bash
# Gunicorn 상태 확인
sudo systemctl status gunicorn
# 로그 확인
sudo journalctl -u gunicorn
```

### Static 파일 안 보임
```bash
# collectstatic 다시 실행
python manage.py collectstatic --noinput
# Nginx 재시작
sudo systemctl restart nginx
```

### 권한 문제
```bash
sudo chown -R ubuntu:www-data /home/ubuntu/portfolio
sudo chmod -R 755 /home/ubuntu/portfolio
```
