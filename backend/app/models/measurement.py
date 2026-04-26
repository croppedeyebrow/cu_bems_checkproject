from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, Index, Integer, Numeric, String, func
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base


class Measurement(Base):
    __tablename__ = "measurements"
    __table_args__ = (
        Index("idx_measurements_time", "measured_at"),
        Index("idx_measurements_device_time", "device_id", "measured_at"),
        Index("idx_measurements_metric_time", "metric_code", "measured_at"),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    building_id: Mapped[int] = mapped_column(ForeignKey("buildings.id"), nullable=False)
    floor_id: Mapped[int] = mapped_column(ForeignKey("floors.id"), nullable=False)
    zone_id: Mapped[int] = mapped_column(ForeignKey("zones.id"), nullable=False)
    device_id: Mapped[int] = mapped_column(ForeignKey("devices.id"), nullable=False)
    measured_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    metric_code: Mapped[str] = mapped_column(String(100), nullable=False)
    value_num: Mapped[float] = mapped_column(Numeric(18, 6), nullable=False)
    unit: Mapped[str | None] = mapped_column(String(50), nullable=True)
    quality_flag: Mapped[str | None] = mapped_column(String(50), nullable=True)
    source_file_id: Mapped[int | None] = mapped_column(
        ForeignKey("raw_import_files.id"), nullable=True
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )
