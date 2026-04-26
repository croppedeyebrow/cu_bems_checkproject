# 08. React 대시보드 설계

## 화면 구성

```text
Overview
Floor View
Zone View
Prediction View
Anomaly View
Data Import View
```

## 1. Overview

### KPI 카드

- Today Energy
- Predicted Energy
- Peak Load
- Active Alerts
- AC Ratio

### 차트

- 실제 사용량 vs 예측 사용량
- AC/조명/플러그 부하 비중
- 일별 에너지 사용량 추이
- 최근 이상 이벤트 목록

## 2. Floor View

- 층 선택
- 층별 시간대 사용량
- 층별 부하 비중
- 층 내 구역별 비교
- 층별 이상 이벤트

## 3. Zone View

- 구역 선택
- AC/조명/플러그 사용량
- 온도/습도/조도 변화
- 구역별 예측 결과
- 구역별 이상 이벤트

## 4. Prediction View

- 실제값 vs 예측값
- 예측 오차
- 모델 성능 지표
- 층별/구역별 성능 비교

## 5. Anomaly View

- 이상 이벤트 목록
- 심각도 필터
- 층/구역 필터
- 이상 유형 필터
- 발생 시점 차트 표시

## 6. Data Import View

- CSV 파일 업로드
- 처리 상태 조회
- 파일별 row/column count 확인
- 실패 로그 확인

## 프론트엔드 구현 원칙

- API 타입을 명확히 정의한다.
- 차트 컴포넌트를 재사용 가능하게 만든다.
- 화면은 기능 단위로 분리한다.
- 초기 디자인은 단순하지만 정보 구조를 명확히 한다.
