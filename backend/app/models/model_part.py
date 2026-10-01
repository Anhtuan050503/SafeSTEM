from sqlalchemy import String, Float, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from backend.app.database.base import Base


class ModelPart(Base):
    __tablename__ = "model_parts"

    model_part_id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True
    )

    model_id: Mapped[int] = mapped_column(
        ForeignKey("assembly_models.model_id")
    )

    part_id: Mapped[int] = mapped_column(
        ForeignKey("lego_parts.part_id")
    )

    instance_code: Mapped[str] = mapped_column(String(100))

    color: Mapped[str | None] = mapped_column(
        String(50),
        nullable=True
    )

    position_x: Mapped[float] = mapped_column(Float, default=0)
    position_y: Mapped[float] = mapped_column(Float, default=0)
    position_z: Mapped[float] = mapped_column(Float, default=0)

    rotation_x: Mapped[float] = mapped_column(Float, default=0)
    rotation_y: Mapped[float] = mapped_column(Float, default=0)
    rotation_z: Mapped[float] = mapped_column(Float, default=0)