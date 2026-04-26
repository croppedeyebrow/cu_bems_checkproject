# AGENTS.md

## 역할

이 저장소에서 AI Assistant는 다음 역할을 수행한다.

- 프로젝트 기획 문서를 기준으로 구현 방향을 유지한다.
- 변경 전 관련 문서를 먼저 확인한다.
- 데이터 모델, API, ETL, ML, 프론트엔드 간의 일관성을 유지한다.
- 임의로 기술 스택을 바꾸지 않는다.

## 공통 개발 규칙

1. 설명 가능한 구조를 우선한다.
2. MVP 범위를 벗어나는 기능은 별도 TODO로 남긴다.
3. `docs/`의 설계와 코드가 충돌하면 먼저 사용자에게 설계 변경 이유를 설명한다.
4. DB 구조 변경 시 `docs/04_database_design.md`와 Alembic migration을 함께 갱신한다.
5. API 변경 시 `docs/07_api_design.md`를 함께 갱신한다.
6. 대시보드 요구사항 변경 시 `docs/08_frontend_dashboard.md`를 함께 갱신한다.
7. ML 모델은 성능보다 재현성과 설명 가능성을 우선한다.

## Backend 규칙

- FastAPI는 router 단위로 분리한다.
- DB 접근은 repository/service 계층으로 분리한다.
- API response는 Pydantic schema로 정의한다.
- `measurements` 원본 테이블을 직접 화면 API에서 과도하게 조회하지 않는다.
- 대시보드 API는 집계 테이블을 우선 사용한다.

## Frontend 규칙

- React + TypeScript 기준으로 구현한다.
- 페이지 단위로 `Overview`, `FloorView`, `ZoneView`, `PredictionView`, `AnomalyView`를 분리한다.
- API 타입은 별도 파일로 관리한다.
- 차트 컴포넌트와 데이터 요청 로직을 분리한다.

## Data/ML 규칙

- 원본 CSV는 Raw Layer에 보존한다.
- ETL은 재실행 가능해야 한다.
- 예측 모델의 입력 피처와 평가 지표를 문서화한다.
- 이상탐지 규칙은 message 생성 기준까지 명시한다.
