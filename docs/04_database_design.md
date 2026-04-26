# 04. 데이터베이스 설계

## 설계 원칙

1. 원본 데이터를 보존한다.
2. 서비스용 데이터는 표준화한다.
3. 1분 원본과 1시간 집계를 분리한다.
4. 측정 항목은 컬럼 추가가 아니라 `metric_code`로 구분한다.
5. ML 결과는 원본 측정값과 분리한다.

## ERD 이미지

이미지 파일이 포함되어 있다면 아래 경로에 배치한다.

```text
docs/assets/database_erd_for_smart_building_system.png
```

## 핵심 테이블

### Raw Layer

#### raw_import_files

| 컬럼 | 설명 |
|---|---|
| id | 파일 ID |
| file_name | 파일명 |
| year | 연도 |
| floor_no | 층 번호 |
| row_count | 행 수 |
| column_count | 컬럼 수 |
| uploaded_at | 업로드 시각 |
| status | 처리 상태 |

#### raw_records

| 컬럼 | 설명 |
|---|---|
| id | 원본 행 ID |
| file_id | raw_import_files FK |
| row_number | 원본 행 번호 |
| measured_at | 측정 시각 |
| raw_payload | 원본 행 JSON |
| created_at | 생성 시각 |

### Master Layer

#### buildings

건물 정보를 저장한다.

#### floors

층 정보를 저장한다.

#### zones

구역 정보를 저장한다.

#### devices

계량기, 센서, 가상 장치를 저장한다.

### Measurement Layer

#### measurements

| 컬럼 | 설명 |
|---|---|
| id | 측정값 ID |
| building_id | 건물 FK |
| floor_id | 층 FK |
| zone_id | 구역 FK |
| device_id | 장치 FK |
| measured_at | 측정 시각 |
| metric_code | 측정 항목 코드 |
| value_num | 측정값 |
| unit | 단위 |
| quality_flag | 품질 플래그 |
| source_file_id | 원본 파일 FK |
| created_at | 생성 시각 |

### Aggregation Layer

#### hourly_zone_energy

구역별 1시간 집계.

#### hourly_floor_energy

층별 1시간 집계.

#### daily_building_energy

건물 일별 집계.

### ML Result Layer

#### prediction_results

예측 결과 저장.

#### anomaly_events

이상탐지 결과 저장.

## 주요 관계

```text
raw_import_files 1:N raw_records
raw_import_files 1:N measurements

buildings 1:N floors
buildings 1:N zones
floors 1:N zones
zones 1:N devices
devices 1:N measurements

buildings/floors/zones 1:N hourly_zone_energy
buildings/floors 1:N hourly_floor_energy
buildings 1:N daily_building_energy

buildings/floors/zones 1:N prediction_results
buildings/floors/zones/devices 1:N anomaly_events
```

## Index 후보

```sql
CREATE INDEX idx_measurements_time ON measurements (measured_at);
CREATE INDEX idx_measurements_device_time ON measurements (device_id, measured_at);
CREATE INDEX idx_measurements_metric_time ON measurements (metric_code, measured_at);
CREATE INDEX idx_hourly_zone_time ON hourly_zone_energy (zone_id, hour_start);
CREATE INDEX idx_hourly_floor_time ON hourly_floor_energy (floor_id, hour_start);
CREATE INDEX idx_anomaly_time ON anomaly_events (start_time, severity);
```

## jsonb 사용 위치

- `raw_records.raw_payload`
- `buildings.metadata`
- `floors.metadata`
- `zones.metadata`
- `devices.metadata`

단, 자주 조회하는 핵심 값은 jsonb에 숨기지 말고 일반 컬럼으로 분리한다.
