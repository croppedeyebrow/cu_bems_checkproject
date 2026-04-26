# 05. ETL 파이프라인 설계

## 목표

CU-BEMS CSV 파일을 읽어 원본 보존, 표준화 저장, 시간 단위 집계까지 처리한다.

## 처리 단계

```text
1. 파일 등록
2. 원본 행 저장
3. 컬럼 패턴 분석
4. 건물/층/구역 생성
5. 장치/센서 생성
6. measurements 저장
7. hourly 집계 생성
8. 처리 상태 업데이트
```

## 파일 등록

`raw_import_files`에 파일명, 연도, 층, 행 수, 컬럼 수, 상태를 저장한다.

## 원본 행 저장

각 행은 `raw_records.raw_payload`에 JSON으로 저장한다.

## 컬럼 파싱

컬럼명에서 다음 정보를 추출한다.

- floor
- zone
- load_type
- metric_type
- device_code

## 측정값 저장

모든 측정값은 `measurements`에 long-format으로 저장한다.

예시:

| measured_at | metric_code | value_num | unit |
|---|---|---:|---|
| 2019-01-01 10:00 | ac_power_kw | 1.25 | kW |
| 2019-01-01 10:00 | temperature_c | 24.8 | °C |

## kWh 집계

1분 단위 power_kw를 1시간 energy_kwh로 변환한다.

```text
hourly_energy_kwh = sum(power_kw_per_minute) / 60
```

## 품질 플래그

| flag | 의미 |
|---|---|
| normal | 정상 |
| missing | 결측 |
| interpolated | 보간 |
| anomaly_candidate | 이상 후보 |

## 재실행 원칙

ETL은 동일 파일을 중복 처리하지 않도록 file checksum 또는 file_name + year + floor_no 기준으로 처리 여부를 확인한다.
