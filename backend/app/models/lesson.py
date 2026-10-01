from datetime import datetime

from sqlalchemy import String, Text, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from backend.app.database.base import Base


class Lesson(Base):
    __tablename__ = "lessons"

    lesson_id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True
    )

    teacher_id: Mapped[int] = mapped_column(
        ForeignKey("users.user_id")
    )

    model_id: Mapped[int] = mapped_column(
        ForeignKey("assembly_models.model_id")
    )

    title: Mapped[str] = mapped_column(String(200))

    description: Mapped[str | None] = mapped_column(
        Text,
        nullable=True
    )

    status: Mapped[str] = mapped_column(
        String(20),
        default="DRAFT"
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.now
    )