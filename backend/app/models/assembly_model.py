from datetime import datetime

from sqlalchemy import String, Text, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from backend.app.database.base import Base


class AssemblyModel(Base):
    __tablename__ = "assembly_models"

    model_id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True
    )

    teacher_id: Mapped[int] = mapped_column(
        ForeignKey("users.user_id")
    )

    kit_id: Mapped[int] = mapped_column(
        ForeignKey("lego_kits.kit_id")
    )

    name: Mapped[str] = mapped_column(String(150))

    description: Mapped[str | None] = mapped_column(
        Text,
        nullable=True
    )

    model_url: Mapped[str | None] = mapped_column(
        String(500),
        nullable=True
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.now
    )