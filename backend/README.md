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
