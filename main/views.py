from django.shortcuts import render

def index(request):
    context = {
        'name': '강동현',
        'title': 'AI를 활용해 문제를 해결하는 개발자',
        'email': 'kangdh318@gmail.com',
        'phone': '+82 010 2179 0151',
        'github': 'https://github.com/kangdh208',
        'about': [
            '문제 해결에 주도적으로 나서고, 새로운 기술에 두려움 없이 도전하며 사람들과 협업을 통해 함께 성장하는 것을 중요시하는 개발자입니다. 특히 LLM과 MCP(Model Context Protocol) 기반의 AI 도구를 실무에 적극적으로 활용하여 개발 생산성과 문제 해결 속도를 끌어올립니다.',
            '다양한 방법을 탐색하고 현실적인 해결책을 찾아 적용하는 일에 흥미를 느끼며, AI를 단순한 코드 생성 도구가 아닌 설계·분석·자동화까지 아우르는 협업 파트너로 활용합니다.',
            '팀에 저의 열정과 AI 활용 역량으로 가치를 더하고, 커뮤니케이션과 문제 해결 능력으로 기여하겠습니다.'
        ],
        'skills': {
            'backend': ['Java', 'SpringBoot', 'Python', 'Django', 'JavaScript'],
            'database': ['MySQL', 'PostgreSQL', 'Redis', 'NoSQL'],
            'ai': ['Claude / Claude Code', 'ChatGPT / Codex', 'Gemini', 'MCP (Model Context Protocol)', 'LLM API 연동', 'RAG', 'Prompt Engineering', 'Cursor', 'AI Pair Programming'],
            'cloud': ['AWS (Lambda, S3, RDS, EC2)', 'Heroku'],
            'tools': ['Git', 'GitHub', 'IntelliJ', 'VSCode', 'PyCharm']
        },
        'education': [
            {'period': '2023.04 ~ 2023.07', 'title': '항해99 부트캠프 14기 수료'},
            {'period': '2014 ~ 2020', 'title': '제주대학교 사범대학 수학교육과 졸업'}
        ],
        'work': {
            'company': 'KUSRC',
            'period': '2024.01 ~ 2026.06',
            'position': '디지털 전환(DX)·AI 전환(AX) 및 데이터 엔지니어링',
            'description': '고객사의 레거시 데이터를 현대적인 디지털 환경으로 전환(DX)하는 동시에, LLM·MCP 기반의 AI를 업무 프로세스에 도입하는 AI 전환(AX) 프로젝트를 주도. 데이터베이스 구조 분석과 ETL 파이프라인 구축부터, AI를 활용한 업무 자동화·문서 처리·의사결정 지원 시스템 개발까지 전 과정을 담당.',
            'achievements': [
                '3개의 대규모 디지털 전환(DX) 프로젝트 성공적 완수',
                'LLM·MCP 기반 AI 전환(AX)으로 고객사 반복 업무 자동화 및 처리 시간 단축',
                '5개 프로젝트의 안정적인 운영 및 지속적인 개선',
                'AI 코딩 도구를 활용한 개발 생산성 향상 및 서버리스 아키텍처 기반 인프라 비용 절감'
            ],
            'tasks': [
                '고객사의 다양한 데이터베이스(RDBMS, NoSQL 등) 구조 및 스키마 분석',
                'Python 기반 ETL 파이프라인 설계·구현으로 데이터 추출(Extract)·변환(Transform)·적재(Load) 자동화',
                'LLM API와 MCP(Model Context Protocol)를 활용한 AI 에이전트 및 업무 자동화 도구 개발',
                'RAG와 프롬프트 엔지니어링을 통한 고객사 문서·데이터 기반 AI 검색/응답 시스템 구축',
                'Claude Code 등 AI 페어 프로그래밍 도입으로 개발 속도 및 코드 품질 개선',
                'RESTful API 설계·개발과 AWS 서버리스 아키텍처 기반 배포, CI/CD 자동화 파이프라인 구축'
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
            {'title': 'AI 활용 역량', 'description': 'LLM, MCP, RAG 등 최신 AI 기술을 실무에 적용하고, Claude Code·Cursor 등 AI 코딩 도구로 개발 생산성을 극대화'},
            {'title': '풀스택 개발 역량', 'description': 'Python과 JavaScript를 활용한 백엔드부터 프론트엔드까지 전 영역 개발 가능'},
            {'title': '클라우드 네이티브', 'description': 'Heroku, AWS 등 서버리스 환경에서의 웹 애플리케이션 설계, 개발, 배포 경험'},
            {'title': '데이터 엔지니어링', 'description': '복잡한 데이터베이스 구조 분석 및 효율적인 ETL 프로세스 구축 능력'},
            {'title': 'DX·AX 전환 역량', 'description': '고객사의 레거시 시스템을 현대적 디지털 환경으로 전환(DX)하고, AI를 도입해 업무를 자동화·고도화하는 AX 프로젝트 수행 경험'},
            {'title': '협업 및 커뮤니케이션', 'description': '팀원들과의 원활한 소통으로 프로젝트 목표 달성에 기여하며, 코드 리뷰와 지식 공유를 통한 팀 성장 주도'},
            {'title': '지속적인 학습', 'description': '새로운 기술 트렌드를 빠르게 습득하고 실무에 적용하여 개발 생산성과 코드 품질 향상에 기여'}
        ]
    }
    return render(request, 'index.html', context)
