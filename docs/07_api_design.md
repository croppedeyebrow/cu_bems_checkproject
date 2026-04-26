# 07. FastAPI API 설계

## API Prefix

```text
/api
```

## 1. Import API

| Method | Endpoint | 설명 |
|---|---|---|
| POST | /api/import/files | CSV 파일 업로드 |
| GET | /api/import/files | 업로드 파일 목록 |
| POST | /api/import/files/{file_id}/process | 파일 처리 |
| GET | /api/import/files/{file_id}/status | 처리 상태 |

## 2. Metadata API

| Method | Endpoint | 설명 |
|---|---|---|
| GET | /api/buildings | 건물 목록 |
| GET | /api/floors | 층 목록 |
| GET | /api/floors/{floor_id}/zones | 층의 구역 목록 |
| GET | /api/zones/{zone_id}/devices | 구역의 장치 목록 |

## 3. Dashboard API

| Method | Endpoint | 설명 |
|---|---|---|
| GET | /api/dashboard/overview | 전체 요약 |
| GET | /api/dashboard/load-breakdown | 부하 비중 |
| GET | /api/dashboard/hourly-trend | 시간별 추이 |
| GET | /api/dashboard/daily-trend | 일별 추이 |
| GET | /api/dashboard/alerts | 최근 경보 |

## 4. Floor/Zone API

| Method | Endpoint | 설명 |
|---|---|---|
| GET | /api/floors/{floor_id}/energy/hourly | 층별 시간대 에너지 |
| GET | /api/floors/{floor_id}/zones/comparison | 층 내 구역 비교 |
| GET | /api/zones/{zone_id}/energy/hourly | 구역별 에너지 |
| GET | /api/zones/{zone_id}/environment/hourly | 구역별 환경 센서 |

## 5. Prediction API

| Method | Endpoint | 설명 |
|---|---|---|
| POST | /api/models/train | 모델 학습 |
| GET | /api/predictions/floors/{floor_id} | 층별 예측 결과 |
| GET | /api/predictions/zones/{zone_id} | 구역별 예측 결과 |
| GET | /api/models/performance | 모델 성능 |

## 6. Anomaly API

| Method | Endpoint | 설명 |
|---|---|---|
| POST | /api/anomalies/detect | 이상탐지 실행 |
| GET | /api/anomalies | 이상 이벤트 목록 |
| GET | /api/anomalies/recent | 최근 이상 이벤트 |
| GET | /api/anomalies/{event_id} | 이상 이벤트 상세 |

## Response 원칙

- 날짜 범위 필터를 지원한다.
- floor_id, zone_id 필터를 지원한다.
- 대시보드 API는 집계 테이블을 사용한다.
- 큰 원본 데이터는 페이지네이션 또는 기간 제한을 적용한다.
