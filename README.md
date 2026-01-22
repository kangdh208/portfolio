# 강동현 포트폴리오

Django로 만든 개인 포트폴리오 웹사이트입니다.

## 기술 스택

- **Backend**: Python, Django
- **Frontend**: HTML5, CSS3, JavaScript
- **Design**: Custom CSS with CSS Variables, Responsive Design

## 설치 및 실행

### 1. 의존성 설치

```bash
pip install -r requirements.txt
```

### 2. 마이그레이션 실행

```bash
python manage.py migrate
```

### 3. 개발 서버 실행

```bash
python manage.py runserver
```

브라우저에서 `http://127.0.0.1:8000` 접속

## 프로젝트 구조

```
portfolio/
├── portfolio/           # Django 프로젝트 설정
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── main/               # 메인 앱
│   ├── views.py        # 포트폴리오 데이터 및 뷰
│   └── urls.py
├── templates/          # HTML 템플릿
│   └── index.html
├── static/             # 정적 파일
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── main.js
├── requirements.txt
└── manage.py
```

## 기능

- 반응형 디자인 (모바일, 태블릿, 데스크톱)
- 다크 테마 UI
- 스크롤 애니메이션
- 모바일 네비게이션 메뉴

## 커스터마이징

`main/views.py` 파일의 `context` 딕셔너리를 수정하여 포트폴리오 내용을 변경할 수 있습니다.

## 라이선스

MIT License
