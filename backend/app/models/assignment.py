from datetime import datetime

from sqlalchemy import String, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from backend.app.database.base import Base


class Assignment(Base):
    __tablename__ = "assignments"

    assignment_id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True
    )

    lesson_id: Mapped[int] = mapped_column(
        ForeignKey("lessons.lesson_id")
    )

    student_id: Mapped[int] = mapped_column(
        ForeignKey("users.user_id")
    )

    assigned_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.now
    )

    due_at: Mapped[datetime | None] = mapped_column(
        DateTime,
        nullable=True
    )

    status: Mapped[str] = mapped_column(
        String(30),
        default="ASSIGNED"
    )

    completed_at: Mapped[datetime | None] = mapped_column(
        DateTime,
        nullable=True
    )