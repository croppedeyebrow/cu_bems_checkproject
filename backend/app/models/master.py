from datetime import datetime
from typing import Any

from sqlalchemy import DateTime, Float, ForeignKey, Integer, String, UniqueConstraint, func
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base


class Building(Base):
    __tablename__ = "buildings"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    building_code: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    building_name: Mapped[str] = mapped_column(String(255), nullable=False)
    location: Mapped[str | None] = mapped_column(String(255), nullable=True)
    area_m2: Mapped[float | None] = mapped_column(Float, nullable=True)
    metadata_json: Mapped[dict[str, Any] | None] = mapped_column("metadata", JSONB, nullable=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )

    floors: Mapped[list["Floor"]] = relationship(back_populates="building")
    zones: Mapped[list["Zone"]] = relationship(back_populates="building")
    devices: Mapped[list["Device"]] = relationship(back_populates="building")


class Floor(Base):
    __tablename__ = "floors"
    __table_args__ = (UniqueConstraint("building_id", "floor_no", name="uq_floors_building_floor"),)

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    building_id: Mapped[int] = mapped_column(ForeignKey("buildings.id"), nullable=False)
    floor_no: Mapped[int] = mapped_column(Integer, nullable=False)
    floor_name: Mapped[str | None] = mapped_column(String(255), nullable=True)
    metadata_json: Mapped[dict[str, Any] | None] = mapped_column("metadata", JSONB, nullable=True)

    building: Mapped["Building"] = relationship(back_populates="floors")
    zones: Mapped[list["Zone"]] = relationship(back_populates="floor")
    devices: Mapped[list["Device"]] = relationship(back_populates="floor")


class Zone(Base):
    __tablename__ = "zones"
    __table_args__ = (
        UniqueConstraint("building_id", "floor_id", "zone_code", name="uq_zones_code_per_floor"),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    building_id: Mapped[int] = mapped_column(ForeignKey("buildings.id"), nullable=False)
    floor_id: Mapped[int] = mapped_column(ForeignKey("floors.id"), nullable=False)
    zone_code: Mapped[str] = mapped_column(String(100), nullable=False)
    zone_name: Mapped[str | None] = mapped_column(String(255), nullable=True)
    metadata_json: Mapped[dict[str, Any] | None] = mapped_column("metadata", JSONB, nullable=True)

    building: Mapped["Building"] = relationship(back_populates="zones")
    floor: Mapped["Floor"] = relationship(back_populates="zones")
    devices: Mapped[list["Device"]] = relationship(back_populates="zone")


class Device(Base):
    __tablename__ = "devices"
    __table_args__ = (
        UniqueConstraint("building_id", "floor_id", "zone_id", "device_code", name="uq_devices_code"),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    building_id: Mapped[int] = mapped_column(ForeignKey("buildings.id"), nullable=False)
    floor_id: Mapped[int] = mapped_column(ForeignKey("floors.id"), nullable=False)
    zone_id: Mapped[int] = mapped_column(ForeignKey("zones.id"), nullable=False)
    device_code: Mapped[str] = mapped_column(String(100), nullable=False)
    device_type: Mapped[str | None] = mapped_column(String(100), nullable=True)
    load_type: Mapped[str | None] = mapped_column(String(100), nullable=True)
    metric_type: Mapped[str | None] = mapped_column(String(100), nullable=True)
    metadata_json: Mapped[dict[str, Any] | None] = mapped_column("metadata", JSONB, nullable=True)

    building: Mapped["Building"] = relationship(back_populates="devices")
    floor: Mapped["Floor"] = relationship(back_populates="devices")
    zone: Mapped["Zone"] = relationship(back_populates="devices")
