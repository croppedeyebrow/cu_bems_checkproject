# PROJECT_CONTEXT

이 파일은 Cursor가 프로젝트 전체 맥락을 빠르게 파악하도록 돕기 위한 요약 문서입니다.

## 프로젝트명

CU-BEMS 기반 스마트빌딩 에너지 예측·이상탐지 디지털트윈 대시보드

## 프로젝트 목표

단순 데이터 분석 노트북이 아니라, CU-BEMS 스마트빌딩 데이터를 기반으로 실제 운영형 데이터 서비스를 구현한다.

## 핵심 데이터 흐름

```text
CU-BEMS CSV
→ Raw Layer
→ ETL / Parser
→ PostgreSQL Core Tables
→ Hourly/Daily Aggregation
→ ML Prediction / Anomaly Detection
→ FastAPI
→ React Dashboard
```

## 핵심 설계 원칙

1. 원본 CSV는 반드시 Raw Layer에 보존한다.
2. 서비스용 데이터는 건물-층-구역-장치-측정값 구조로 표준화한다.
3. 1분 단위 원본 데이터와 대시보드용 집계 데이터를 분리한다.
4. 대시보드는 원본 `measurements`보다 집계 테이블을 우선 조회한다.
5. ML 결과는 별도 테이블에 저장한다.
6. API는 화면 요구사항과 데이터 계층을 분리한다.
7. MVP에서는 인증/권한보다 데이터 파이프라인과 대시보드를 우선한다.

## MVP 범위

- 2019년 CU-BEMS 데이터 우선 처리
- 1시간 단위 집계
- 층별/구역별/부하별 에너지 모니터링
- 층별 전력 사용량 예측
- 규칙 기반 이상탐지
- React 대시보드 기본 화면

## 개발 우선순위

1. DB schema
2. ETL import
3. Aggregation
4. API
5. Prediction
6. Anomaly detection
7. Dashboard
8. Docker deployment
