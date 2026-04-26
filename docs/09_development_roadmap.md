# 09. 개발 로드맵

## Phase 0. 프로젝트 초기 설정

- Git 저장소 생성
- Cursor에서 프로젝트 열기
- 문서 세트 배치
- `.cursor/rules` 설정
- Python/Node/PostgreSQL 개발환경 확인

## Phase 1. Backend 스캐폴딩

- FastAPI 프로젝트 생성
- 설정 관리
- DB 연결
- SQLAlchemy 설정
- Alembic 설정
- Health check API

## Phase 2. DB Schema

- Raw Layer 테이블
- Master Layer 테이블
- Measurement Layer 테이블
- Aggregation Layer 테이블
- ML Result Layer 테이블
- Index 추가

## Phase 3. ETL

- CSV 업로드
- 파일 메타데이터 저장
- 원본 행 저장
- 컬럼 파싱
- measurements 저장
- 1시간 집계 생성

## Phase 4. API

- Metadata API
- Dashboard API
- Floor/Zone API
- Prediction API
- Anomaly API

## Phase 5. ML

- Feature table 생성
- Baseline 모델
- RandomForest 모델
- 예측 결과 저장
- 모델 성능 조회

## Phase 6. 이상탐지

- 규칙 기반 탐지
- 예측 오차 기반 탐지
- 이상 이벤트 저장
- 경보 API

## Phase 7. Frontend

- Vite + React + TypeScript 구성
- Layout
- Overview
- Floor View
- Zone View
- Prediction View
- Anomaly View

## Phase 8. Docker/문서화

- docker-compose
- README 정리
- API 명세 정리
- 스크린샷
- 회고 문서

## 가장 먼저 할 일

```text
1. 폴더 구조 생성
2. FastAPI health check
3. PostgreSQL 연결
4. Alembic migration
5. ERD 기준 테이블 생성
```
