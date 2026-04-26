# 03. 전체 아키텍처

## 시스템 흐름

```text
[CU-BEMS CSV Files]
        |
        v
[Raw Import Layer]
- raw_import_files
- raw_records
        |
        v
[ETL / Parser Layer]
- 층 정보 파싱
- 구역 정보 파싱
- 장치/센서 항목 분리
- 단위 표준화
- 결측 처리
        |
        v
[Core Database Layer]
- buildings
- floors
- zones
- devices
- measurements
        |
        v
[Aggregation Layer]
- hourly_zone_energy
- hourly_floor_energy
- daily_building_energy
        |
        v
[ML Layer]
- prediction_results
- anomaly_events
        |
        v
[FastAPI]
        |
        v
[React Dashboard]
```

## 백엔드 권장 구조

```text
backend/
  app/
    main.py
    core/
      config.py
      database.py
    models/
    schemas/
    repositories/
    services/
    api/
      routes/
    etl/
    ml/
    jobs/
  alembic/
  tests/
```

## 프론트엔드 권장 구조

```text
frontend/
  src/
    api/
    components/
      charts/
      cards/
      tables/
    pages/
      Overview/
      FloorView/
      ZoneView/
      PredictionView/
      AnomalyView/
    types/
    hooks/
    utils/
```

## 인프라 구조

```text
infra/
  docker-compose.yml
  postgres/
```

## 주요 설계 방향

- Raw Layer와 Core Layer를 분리한다.
- measurements는 표준화된 long-format 구조를 사용한다.
- 대시보드는 aggregation table을 조회한다.
- ML 결과는 별도 결과 테이블에 저장한다.
