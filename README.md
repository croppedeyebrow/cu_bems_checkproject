# CU-BEMS 기반 스마트빌딩 에너지 예측·이상탐지 디지털트윈 대시보드

## 1. 프로젝트 한 줄 정의

CU-BEMS 스마트빌딩 데이터를 활용해 건물-층-구역-장치-측정값 구조로 데이터를 관리하고, 에너지 사용량 예측과 이상탐지를 제공하는 운영형 대시보드 서비스입니다.

## 2. 핵심 목표

- CU-BEMS 원본 CSV 데이터를 PostgreSQL에 적재
- 1분 단위 데이터를 1시간 단위 분석/대시보드용 데이터로 집계
- 층별/구역별/부하별 에너지 사용량 분석
- 온도, 습도, 조도 등 실내환경 데이터와 전력 사용량 관계 분석
- 에너지 사용량 예측 모델 구현
- 야간 과소비, 예측 오차 이상, 센서 이상 탐지
- FastAPI API와 React 대시보드 구현

## 3. 기술 스택

| 영역          | 기술                                 |
| ------------- | ------------------------------------ |
| Backend       | Python, FastAPI, SQLAlchemy, Alembic |
| Database      | PostgreSQL                           |
| Data/ML       | pandas, scikit-learn                 |
| Frontend      | React, TypeScript, Vite              |
| Visualization | Recharts 또는 ECharts                |
| Infra         | Local Development (Python venv)      |
| IDE           | Cursor                               |

## 4. 문서 구조

| 문서                             | 목적                  |
| -------------------------------- | --------------------- |
| `docs/00_project_overview.md`    | 전체 프로젝트 개요    |
| `docs/01_dataset_cu_bems.md`     | CU-BEMS 데이터셋 설명 |
| `docs/02_requirements.md`        | 기능 요구사항         |
| `docs/03_architecture.md`        | 전체 아키텍처         |
| `docs/04_database_design.md`     | DB 구조와 ERD         |
| `docs/05_etl_pipeline.md`        | 데이터 적재/정제/집계 |
| `docs/06_ml_plan.md`             | 예측/이상탐지 설계    |
| `docs/07_api_design.md`          | FastAPI API 설계      |
| `docs/08_frontend_dashboard.md`  | React 대시보드 설계   |
| `docs/09_development_roadmap.md` | 개발 로드맵           |
| `docs/10_cursor_workflow.md`     | Cursor 활용 방식      |
| `docs/11_definition_of_done.md`  | 완료 기준             |

## 5. 첫 개발 목표

첫 번째 목표는 화면 구현이 아니라 데이터 기반을 잡는 것입니다.

```text
1단계: 프로젝트 스캐폴딩
2단계: PostgreSQL + Alembic 설정
3단계: CU-BEMS 메타데이터 테이블 생성
4단계: CSV 적재 파이프라인 작성
5단계: hourly 집계 테이블 생성
```

## 6. 현재 개발 모드

현재 단계는 프론트엔드 구현보다 **백엔드와 데이터 파이프라인 기반 구축**에 집중한다.
실행 환경은 Docker가 아닌 로컬 개발 환경(venv + PostgreSQL) 기준으로 운영한다.
