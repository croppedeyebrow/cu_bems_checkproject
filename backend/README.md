# Backend

## 기술

- Python
- FastAPI
- SQLAlchemy
- Alembic
- PostgreSQL
- pandas
- scikit-learn

## 권장 구조

```text
backend/
  app/
    main.py
    core/
    models/
    schemas/
    repositories/
    services/
    api/routes/
    etl/
    ml/
    jobs/
  alembic/
  tests/
```

## 첫 구현 목표

1. FastAPI 앱 생성
2. `/health` API
3. PostgreSQL 연결
4. Alembic 설정
5. ERD 기준 모델 작성

## 로컬 실행 (백엔드 집중)

프로젝트는 현재 백엔드 중심으로 개발하며, 실행 환경은 로컬 Python 환경을 기본으로 사용한다.

### 실행

`backend` 경로에서 아래 명령으로 FastAPI를 실행한다.

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### 확인

- API: `http://localhost:8000`
- Health Check: `http://localhost:8000/api/health`
- DB: 로컬 PostgreSQL 연결 정보(.env 기준)

## Alembic 마이그레이션

ERD 기준 초기 스키마 리비전 파일:

- `alembic/versions/20260426_1800_initial_schema.py`

적용 명령(`backend` 기준):

```bash
alembic upgrade head
```
