#!/usr/bin/env python
"""
Django 포트폴리오를 Firebase Hosting용 정적 사이트로 빌드한다.

'/' 페이지를 한 번 렌더링해서 public/index.html 로 저장하고,
static/ 자산을 public/static/ 으로 복사한다.

사용법:
    python scripts/build_static.py
    firebase deploy
"""
import os
import sys
import shutil
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
PUBLIC = BASE / "public"

# 프로젝트 루트를 import 경로에 추가 (어느 위치에서 실행해도 동작하도록)
sys.path.insert(0, str(BASE))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "portfolio.settings")
os.environ.setdefault("DEBUG", "False")

import django  # noqa: E402

django.setup()

from django.test.utils import override_settings  # noqa: E402

# 정적 export에서는 해시 매니페스트 스토리지 대신 단순 스토리지를 써서
# {% static %} 경로가 실제 파일명과 그대로 맞아떨어지게 한다.
with override_settings(
    ALLOWED_HOSTS=["*"],
    STATICFILES_STORAGE="django.contrib.staticfiles.storage.StaticFilesStorage",
):
    from django.test import Client

    if PUBLIC.exists():
        shutil.rmtree(PUBLIC)
    PUBLIC.mkdir(parents=True)

    response = Client().get("/")
    if response.status_code != 200:
        raise SystemExit(f"렌더링 실패: HTTP {response.status_code}")
    (PUBLIC / "index.html").write_bytes(response.content)

    shutil.copytree(BASE / "static", PUBLIC / "static")

print(f"빌드 완료 -> {PUBLIC}")
