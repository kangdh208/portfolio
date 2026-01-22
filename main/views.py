from django.shortcuts import render

def index(request):
    context = {
        'name': '강동현',
        'title': '개발을 즐기는 개발자',
        'email': 'kangdh208@gmail.com',
        'phone': '+821071899403',
        'github': 'https://github.com/kangdh208',
        'about': [
            '문제 해결에 주도적으로 나서고, 새로운 기술에 두려움 없이 도전하며 사람들과 협업을 하여 함께 성장하고 발전하는 것을 중요시하는 개발자입니다.',
            '다양한 방법을 탐색하고 현실적인 해결책을 찾고 이를 적용하는 일에 흥미를 느낍니다.',
            '팀에 저의 열정과 노력으로 가치를 더하고 커뮤니케이션과 문제 해결 능력으로 기여할 것입니다.'
        ],
        'skills': {
            'backend': ['Java', 'SpringBoot', 'Python', 'Django', 'JavaScript'],
            'database': ['MySQL', 'PostgreSQL', 'Redis', 'NoSQL'],
            'cloud': ['AWS (Lambda, S3, RDS, EC2)', 'Heroku'],
            'tools': ['Git', 'GitHub', 'IntelliJ', 'VSCode', 'PyCharm']
        },
        'education': [
            {'period': '2023.04 ~ 2023.07', 'title': '항해99 부트캠프 14기 수료'},
            {'period': '2014 ~ 2020', 'title': '제주대학교 사범대학 수학교육과 졸업'}
        ],
        'work': {
            'company': 'KUSRC',
            'period': '2024.01 ~ 현재',
            'position': '고객사 데이터 ETL 및 디지털 트랜스포메이션',
            'description': '고객사의 레거시 데이터를 분석하고 현대적인 디지털 환경으로 전환하는 프로젝트를 수행. 데이터베이스 구조 분석부터 ETL 파이프라인 구축, API 개발, 사용자 친화적인 인터페이스 개발까지 전 과정을 담당.',
            'achievements': [
                '3개의 대규모 디지털 트랜스포메이션 프로젝트 성공적 완수',
                '5개 프로젝트의 안정적인 운영 및 지속적인 개선',
                '서버리스 아키텍처를 활용한 인프라 비용 절감 및 확장성 확보',
                'Python 기반 ETL 파이프라인 자동화로 데이터 처리 효율성 향상'
            ],
            'tasks': [
                '고객사의 다양한 데이터베이스(RDBMS, NoSQL 등) 구조 및 스키마 분석',
                'Python을 활용한 데이터 추출(Extract), 변환(Transform), 적재(Load) 파이프라인 설계 및 구현',
                'RESTful API 설계 및 개발을 통한 클라이언트-서버 통신 구현',
                'Heroku, AWS를 활용한 서버리스 아키텍처 설계 및 배포',
                'CI/CD 파이프라인 구축을 통한 자동화된 배포 프로세스 확립'
            ]
        },
        'projects': [
            {
                'name': 'Moyiza',
                'subtitle': '누구나 열고 참여할 수 있는 취미 공유 플랫폼',
                'github': 'https://github.com/H99-FinalProj-Moyiza/Moyiza_BE',
                'period': '2023.05 ~ 2023.07',
                'tools': ['SpringBoot', 'AWS', 'Github Action', 'CodeDeploy', 'Redis'],
                'features': [
                    '관심사를 기반으로 클럽을 만들고 비슷한 관심사를 가진 사람을 모아 일회성 모임을 열 수 있습니다.',
                    '클럽 없이 일회성 모임만 생성도 가능하며, 클럽과 모임에 참여하면 대화 방에 자동 입장이 됩니다.',
                    '유저의 위치 정보를 기반으로 주변의 모임을 추천합니다.'
                ],
                'contributions': [
                    {
                        'title': 'SSE를 이용한 알림 구현',
                        'details': 'WebSocket 대비 자원 효율적인 SSE를 선택하여 실시간 알림 구현. Jmeter를 사용한 부하 테스트와 백프레셔 메커니즘 도입으로 쓰레드 넘침 문제 해결.'
                    },
                    {
                        'title': 'QueryDSL을 사용한 필터 기능 구현',
                        'details': 'JPA @Query의 정적 쿼리 한계를 극복하기 위해 QueryDSL 도입. 가독성, 유지보수성, 타입 안정성 측면에서 동적 쿼리 작성 효율화.'
                    },
                    {
                        'title': 'UX를 고려한 임시 저장 기능 구현',
                        'details': '모임 생성 시 다양한 정보 입력이 필요한 점을 고려하여 임시 저장 및 불러오기 기능 구현으로 사용자 경험 개선.'
                    }
                ]
            }
        ],
        'core_competencies': [
            {'title': '풀스택 개발 역량', 'description': 'Python과 JavaScript를 활용한 백엔드부터 프론트엔드까지 전 영역 개발 가능'},
            {'title': '클라우드 네이티브', 'description': 'Heroku, AWS 등 서버리스 환경에서의 웹 애플리케이션 설계, 개발, 배포 경험'},
            {'title': '데이터 엔지니어링', 'description': '복잡한 데이터베이스 구조 분석 및 효율적인 ETL 프로세스 구축 능력'},
            {'title': '문제 해결 능력', 'description': '고객사의 레거시 시스템을 현대적인 디지털 환경으로 전환하는 프로젝트 수행 경험'},
            {'title': '협업 및 커뮤니케이션', 'description': '팀원들과의 원활한 소통으로 프로젝트 목표 달성에 기여하며, 코드 리뷰와 지식 공유를 통한 팀 성장 주도'},
            {'title': '지속적인 학습', 'description': '새로운 기술 트렌드를 빠르게 습득하고 실무에 적용하여 개발 생산성과 코드 품질 향상에 기여'}
        ]
    }
    return render(request, 'index.html', context)
