# 10. Cursor 활용 방식

## 목표

Cursor가 프로젝트 맥락을 놓치지 않도록 문서와 규칙을 먼저 제공한다.

## 기본 사용 방식

Cursor 채팅에서 작업을 요청할 때 다음 문서를 함께 참조한다.

```text
@PROJECT_CONTEXT.md
@AGENTS.md
@docs/04_database_design.md
@docs/07_api_design.md
```

## 추천 프롬프트 1: 백엔드 초기화

```text
@PROJECT_CONTEXT.md @AGENTS.md @docs/03_architecture.md

FastAPI 백엔드 프로젝트를 초기화해줘.
backend/app 구조를 만들고, health check API, config, database 연결 파일까지 만들어줘.
아직 비즈니스 로직은 구현하지 말고 구조만 잡아줘.
```

## 추천 프롬프트 2: DB 모델 작성

```text
@docs/04_database_design.md @AGENTS.md

문서의 ERD를 기준으로 SQLAlchemy 모델을 작성해줘.
각 테이블의 PK/FK 관계를 반영하고, Alembic migration이 가능하도록 구성해줘.
```

## 추천 프롬프트 3: ETL 작성

```text
@docs/05_etl_pipeline.md @docs/04_database_design.md

CU-BEMS CSV 파일을 읽어서 raw_import_files, raw_records, measurements에 저장하는 ETL 서비스 초안을 작성해줘.
층/구역/장치 파싱 로직은 함수로 분리하고 테스트 가능하게 만들어줘.
```

## 추천 프롬프트 4: API 작성

```text
@docs/07_api_design.md @docs/04_database_design.md

대시보드 API 라우터를 작성해줘.
overview, load-breakdown, hourly-trend 엔드포인트를 먼저 구현하고, DB 조회는 service 계층으로 분리해줘.
```

## 추천 프롬프트 5: 프론트엔드 작성

```text
@docs/08_frontend_dashboard.md

React + TypeScript 기준으로 Overview 화면을 만들어줘.
KPI 카드, 에너지 추이 차트, 부하 비중 차트, 최근 경보 목록 영역을 구성해줘.
```

## Cursor 사용 원칙

- 한 번에 전체 프로젝트를 만들라고 하지 않는다.
- 문서 하나 또는 기능 하나 단위로 요청한다.
- 생성된 코드가 문서와 맞는지 매번 확인한다.
- DB 구조 변경은 반드시 문서와 migration을 함께 수정한다.
