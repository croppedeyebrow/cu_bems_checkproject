# 06. ML 설계

## 1. 예측 목표

MVP에서는 다음 값을 예측한다.

```text
다음 1시간의 층별 total_energy_kwh
```

확장 단계에서는 다음 값을 예측한다.

- 구역별 total_energy_kwh
- ac_energy_kwh
- lighting_energy_kwh
- plug_energy_kwh

## 2. 입력 피처

| 피처 | 설명 |
|---|---|
| hour | 시간대 |
| day_of_week | 요일 |
| is_weekend | 주말 여부 |
| previous_1h_energy | 1시간 전 전력량 |
| previous_24h_energy | 24시간 전 전력량 |
| rolling_mean_6h | 최근 6시간 평균 |
| rolling_mean_24h | 최근 24시간 평균 |
| avg_temperature_c | 평균 온도 |
| avg_humidity_pct | 평균 습도 |
| avg_illuminance_lux | 평균 조도 |
| ac_ratio | AC 비중 |
| lighting_ratio | 조명 비중 |
| plug_ratio | 플러그 비중 |

## 3. 모델 후보

| 단계 | 모델 |
|---|---|
| Baseline | Linear Regression |
| 기본 모델 | RandomForestRegressor |
| 개선 모델 | GradientBoostingRegressor |
| 선택 | LightGBM 또는 XGBoost |

## 4. 평가 지표

- MAE
- RMSE
- MAPE
- R²

## 5. 이상탐지

### 규칙 기반

- 야간 과소비
- 주말 과소비
- 센서 고정
- 센서 급변
- 결측 지속

### 모델 기반

- Isolation Forest
- Prediction Error
- Z-score

## 6. 결과 저장

예측 결과는 `prediction_results`에 저장한다.

이상탐지 결과는 `anomaly_events`에 저장한다.

## 7. MVP 기준

MVP에서는 복잡한 딥러닝을 사용하지 않는다. 설명 가능한 모델과 규칙 기반 탐지를 먼저 구현한다.
