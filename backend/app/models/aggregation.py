from datetime import date, datetime

from sqlalchemy import Date, DateTime, ForeignKey, Index, Integer, Numeric
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base


class HourlyZoneEnergy(Base):
    __tablename__ = "hourly_zone_energy"
    __table_args__ = (Index("idx_hourly_zone_time", "zone_id", "hour_start"),)

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    building_id: Mapped[int] = mapped_column(ForeignKey("buildings.id"), nullable=False)
    floor_id: Mapped[int] = mapped_column(ForeignKey("floors.id"), nullable=False)
    zone_id: Mapped[int] = mapped_column(ForeignKey("zones.id"), nullable=False)
    hour_start: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    ac_energy_kwh: Mapped[float | None] = mapped_column(Numeric(18, 6), nullable=True)
    lighting_energy_kwh: Mapped[float | None] = mapped_column(Numeric(18, 6), nullable=True)
    plug_energy_kwh: Mapped[float | None] = mapped_column(Numeric(18, 6), nullable=True)
    total_energy_kwh: Mapped[float | None] = mapped_column(Numeric(18, 6), nullable=True)
    avg_temperature_c: Mapped[float | None] = mapped_column(Numeric(10, 4), nullable=True)
    avg_humidity_pct: Mapped[float | None] = mapped_column(Numeric(10, 4), nullable=True)
    avg_illuminance_lux: Mapped[float | None] = mapped_column(Numeric(10, 4), nullable=True)


class HourlyFloorEnergy(Base):
    __tablename__ = "hourly_floor_energy"
    __table_args__ = (Index("idx_hourly_floor_time", "floor_id", "hour_start"),)

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    building_id: Mapped[int] = mapped_column(ForeignKey("buildings.id"), nullable=False)
    floor_id: Mapped[int] = mapped_column(ForeignKey("floors.id"), nullable=False)
    hour_start: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    ac_energy_kwh: Mapped[float | None] = mapped_column(Numeric(18, 6), nullable=True)
    lighting_energy_kwh: Mapped[float | None] = mapped_column(Numeric(18, 6), nullable=True)
    plug_energy_kwh: Mapped[float | None] = mapped_column(Numeric(18, 6), nullable=True)
    total_energy_kwh: Mapped[float | None] = mapped_column(Numeric(18, 6), nullable=True)
    peak_power_kw: Mapped[float | None] = mapped_column(Numeric(18, 6), nullable=True)
    avg_temperature_c: Mapped[float | None] = mapped_column(Numeric(10, 4), nullable=True)
    avg_humidity_pct: Mapped[float | None] = mapped_column(Numeric(10, 4), nullable=True)
    avg_illuminance_lux: Mapped[float | None] = mapped_column(Numeric(10, 4), nullable=True)


class DailyBuildingEnergy(Base):
    __tablename__ = "daily_building_energy"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    building_id: Mapped[int] = mapped_column(ForeignKey("buildings.id"), nullable=False)
    date: Mapped[date] = mapped_column(Date, nullable=False)
    ac_energy_kwh: Mapped[float | None] = mapped_column(Numeric(18, 6), nullable=True)
    lighting_energy_kwh: Mapped[float | None] = mapped_column(Numeric(18, 6), nullable=True)
    plug_energy_kwh: Mapped[float | None] = mapped_column(Numeric(18, 6), nullable=True)
    total_energy_kwh: Mapped[float | None] = mapped_column(Numeric(18, 6), nullable=True)
    peak_power_kw: Mapped[float | None] = mapped_column(Numeric(18, 6), nullable=True)
    avg_temperature_c: Mapped[float | None] = mapped_column(Numeric(10, 4), nullable=True)
