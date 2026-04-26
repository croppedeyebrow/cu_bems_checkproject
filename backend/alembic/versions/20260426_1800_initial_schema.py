"""initial schema

Revision ID: 20260426_1800
Revises:
Create Date: 2026-04-26 18:00:00
"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = "20260426_1800"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "raw_import_files",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("file_name", sa.String(length=255), nullable=False),
        sa.Column("year", sa.Integer(), nullable=False),
        sa.Column("floor_no", sa.Integer(), nullable=False),
        sa.Column("row_count", sa.Integer(), nullable=True),
        sa.Column("column_count", sa.Integer(), nullable=True),
        sa.Column("uploaded_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=False),
        sa.Column("status", sa.String(length=50), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )

    op.create_table(
        "buildings",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("building_code", sa.String(length=100), nullable=False),
        sa.Column("building_name", sa.String(length=255), nullable=False),
        sa.Column("location", sa.String(length=255), nullable=True),
        sa.Column("area_m2", sa.Float(), nullable=True),
        sa.Column("metadata", postgresql.JSONB(astext_type=sa.Text()), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("building_code"),
    )

    op.create_table(
        "raw_records",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("file_id", sa.Integer(), nullable=False),
        sa.Column("row_number", sa.Integer(), nullable=False),
        sa.Column("measured_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("raw_payload", postgresql.JSONB(astext_type=sa.Text()), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=False),
        sa.ForeignKeyConstraint(["file_id"], ["raw_import_files.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
    )

    op.create_table(
        "floors",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("building_id", sa.Integer(), nullable=False),
        sa.Column("floor_no", sa.Integer(), nullable=False),
        sa.Column("floor_name", sa.String(length=255), nullable=True),
        sa.Column("metadata", postgresql.JSONB(astext_type=sa.Text()), nullable=True),
        sa.ForeignKeyConstraint(["building_id"], ["buildings.id"]),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("building_id", "floor_no", name="uq_floors_building_floor"),
    )

    op.create_table(
        "zones",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("building_id", sa.Integer(), nullable=False),
        sa.Column("floor_id", sa.Integer(), nullable=False),
        sa.Column("zone_code", sa.String(length=100), nullable=False),
        sa.Column("zone_name", sa.String(length=255), nullable=True),
        sa.Column("metadata", postgresql.JSONB(astext_type=sa.Text()), nullable=True),
        sa.ForeignKeyConstraint(["building_id"], ["buildings.id"]),
        sa.ForeignKeyConstraint(["floor_id"], ["floors.id"]),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("building_id", "floor_id", "zone_code", name="uq_zones_code_per_floor"),
    )

    op.create_table(
        "devices",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("building_id", sa.Integer(), nullable=False),
        sa.Column("floor_id", sa.Integer(), nullable=False),
        sa.Column("zone_id", sa.Integer(), nullable=False),
        sa.Column("device_code", sa.String(length=100), nullable=False),
        sa.Column("device_type", sa.String(length=100), nullable=True),
        sa.Column("load_type", sa.String(length=100), nullable=True),
        sa.Column("metric_type", sa.String(length=100), nullable=True),
        sa.Column("metadata", postgresql.JSONB(astext_type=sa.Text()), nullable=True),
        sa.ForeignKeyConstraint(["building_id"], ["buildings.id"]),
        sa.ForeignKeyConstraint(["floor_id"], ["floors.id"]),
        sa.ForeignKeyConstraint(["zone_id"], ["zones.id"]),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("building_id", "floor_id", "zone_id", "device_code", name="uq_devices_code"),
    )

    op.create_table(
        "measurements",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("building_id", sa.Integer(), nullable=False),
        sa.Column("floor_id", sa.Integer(), nullable=False),
        sa.Column("zone_id", sa.Integer(), nullable=False),
        sa.Column("device_id", sa.Integer(), nullable=False),
        sa.Column("measured_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("metric_code", sa.String(length=100), nullable=False),
        sa.Column("value_num", sa.Numeric(precision=18, scale=6), nullable=False),
        sa.Column("unit", sa.String(length=50), nullable=True),
        sa.Column("quality_flag", sa.String(length=50), nullable=True),
        sa.Column("source_file_id", sa.Integer(), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=False),
        sa.ForeignKeyConstraint(["building_id"], ["buildings.id"]),
        sa.ForeignKeyConstraint(["device_id"], ["devices.id"]),
        sa.ForeignKeyConstraint(["floor_id"], ["floors.id"]),
        sa.ForeignKeyConstraint(["source_file_id"], ["raw_import_files.id"]),
        sa.ForeignKeyConstraint(["zone_id"], ["zones.id"]),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index("idx_measurements_time", "measurements", ["measured_at"], unique=False)
    op.create_index("idx_measurements_device_time", "measurements", ["device_id", "measured_at"], unique=False)
    op.create_index("idx_measurements_metric_time", "measurements", ["metric_code", "measured_at"], unique=False)

    op.create_table(
        "hourly_zone_energy",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("building_id", sa.Integer(), nullable=False),
        sa.Column("floor_id", sa.Integer(), nullable=False),
        sa.Column("zone_id", sa.Integer(), nullable=False),
        sa.Column("hour_start", sa.DateTime(timezone=True), nullable=False),
        sa.Column("ac_energy_kwh", sa.Numeric(precision=18, scale=6), nullable=True),
        sa.Column("lighting_energy_kwh", sa.Numeric(precision=18, scale=6), nullable=True),
        sa.Column("plug_energy_kwh", sa.Numeric(precision=18, scale=6), nullable=True),
        sa.Column("total_energy_kwh", sa.Numeric(precision=18, scale=6), nullable=True),
        sa.Column("avg_temperature_c", sa.Numeric(precision=10, scale=4), nullable=True),
        sa.Column("avg_humidity_pct", sa.Numeric(precision=10, scale=4), nullable=True),
        sa.Column("avg_illuminance_lux", sa.Numeric(precision=10, scale=4), nullable=True),
        sa.ForeignKeyConstraint(["building_id"], ["buildings.id"]),
        sa.ForeignKeyConstraint(["floor_id"], ["floors.id"]),
        sa.ForeignKeyConstraint(["zone_id"], ["zones.id"]),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index("idx_hourly_zone_time", "hourly_zone_energy", ["zone_id", "hour_start"], unique=False)

    op.create_table(
        "hourly_floor_energy",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("building_id", sa.Integer(), nullable=False),
        sa.Column("floor_id", sa.Integer(), nullable=False),
        sa.Column("hour_start", sa.DateTime(timezone=True), nullable=False),
        sa.Column("ac_energy_kwh", sa.Numeric(precision=18, scale=6), nullable=True),
        sa.Column("lighting_energy_kwh", sa.Numeric(precision=18, scale=6), nullable=True),
        sa.Column("plug_energy_kwh", sa.Numeric(precision=18, scale=6), nullable=True),
        sa.Column("total_energy_kwh", sa.Numeric(precision=18, scale=6), nullable=True),
        sa.Column("peak_power_kw", sa.Numeric(precision=18, scale=6), nullable=True),
        sa.Column("avg_temperature_c", sa.Numeric(precision=10, scale=4), nullable=True),
        sa.Column("avg_humidity_pct", sa.Numeric(precision=10, scale=4), nullable=True),
        sa.Column("avg_illuminance_lux", sa.Numeric(precision=10, scale=4), nullable=True),
        sa.ForeignKeyConstraint(["building_id"], ["buildings.id"]),
        sa.ForeignKeyConstraint(["floor_id"], ["floors.id"]),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index("idx_hourly_floor_time", "hourly_floor_energy", ["floor_id", "hour_start"], unique=False)

    op.create_table(
        "daily_building_energy",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("building_id", sa.Integer(), nullable=False),
        sa.Column("date", sa.Date(), nullable=False),
        sa.Column("ac_energy_kwh", sa.Numeric(precision=18, scale=6), nullable=True),
        sa.Column("lighting_energy_kwh", sa.Numeric(precision=18, scale=6), nullable=True),
        sa.Column("plug_energy_kwh", sa.Numeric(precision=18, scale=6), nullable=True),
        sa.Column("total_energy_kwh", sa.Numeric(precision=18, scale=6), nullable=True),
        sa.Column("peak_power_kw", sa.Numeric(precision=18, scale=6), nullable=True),
        sa.Column("avg_temperature_c", sa.Numeric(precision=10, scale=4), nullable=True),
        sa.ForeignKeyConstraint(["building_id"], ["buildings.id"]),
        sa.PrimaryKeyConstraint("id"),
    )

    op.create_table(
        "prediction_results",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("building_id", sa.Integer(), nullable=False),
        sa.Column("floor_id", sa.Integer(), nullable=True),
        sa.Column("zone_id", sa.Integer(), nullable=True),
        sa.Column("target_metric", sa.String(length=100), nullable=False),
        sa.Column("model_name", sa.String(length=100), nullable=False),
        sa.Column("model_version", sa.String(length=50), nullable=True),
        sa.Column("predicted_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("target_time", sa.DateTime(timezone=True), nullable=False),
        sa.Column("predicted_value", sa.Numeric(precision=18, scale=6), nullable=False),
        sa.Column("actual_value", sa.Numeric(precision=18, scale=6), nullable=True),
        sa.Column("error_value", sa.Numeric(precision=18, scale=6), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=False),
        sa.ForeignKeyConstraint(["building_id"], ["buildings.id"]),
        sa.ForeignKeyConstraint(["floor_id"], ["floors.id"]),
        sa.ForeignKeyConstraint(["zone_id"], ["zones.id"]),
        sa.PrimaryKeyConstraint("id"),
    )

    op.create_table(
        "anomaly_events",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("building_id", sa.Integer(), nullable=False),
        sa.Column("floor_id", sa.Integer(), nullable=True),
        sa.Column("zone_id", sa.Integer(), nullable=True),
        sa.Column("device_id", sa.Integer(), nullable=True),
        sa.Column("metric_code", sa.String(length=100), nullable=False),
        sa.Column("start_time", sa.DateTime(timezone=True), nullable=False),
        sa.Column("end_time", sa.DateTime(timezone=True), nullable=True),
        sa.Column("severity", sa.String(length=50), nullable=False),
        sa.Column("anomaly_score", sa.Numeric(precision=10, scale=4), nullable=True),
        sa.Column("detection_method", sa.String(length=100), nullable=True),
        sa.Column("message", sa.String(length=1000), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=False),
        sa.ForeignKeyConstraint(["building_id"], ["buildings.id"]),
        sa.ForeignKeyConstraint(["device_id"], ["devices.id"]),
        sa.ForeignKeyConstraint(["floor_id"], ["floors.id"]),
        sa.ForeignKeyConstraint(["zone_id"], ["zones.id"]),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index("idx_anomaly_time", "anomaly_events", ["start_time", "severity"], unique=False)


def downgrade() -> None:
    op.drop_index("idx_anomaly_time", table_name="anomaly_events")
    op.drop_table("anomaly_events")
    op.drop_table("prediction_results")
    op.drop_table("daily_building_energy")
    op.drop_index("idx_hourly_floor_time", table_name="hourly_floor_energy")
    op.drop_table("hourly_floor_energy")
    op.drop_index("idx_hourly_zone_time", table_name="hourly_zone_energy")
    op.drop_table("hourly_zone_energy")
    op.drop_index("idx_measurements_metric_time", table_name="measurements")
    op.drop_index("idx_measurements_device_time", table_name="measurements")
    op.drop_index("idx_measurements_time", table_name="measurements")
    op.drop_table("measurements")
    op.drop_table("devices")
    op.drop_table("zones")
    op.drop_table("floors")
    op.drop_table("raw_records")
    op.drop_table("buildings")
    op.drop_table("raw_import_files")
