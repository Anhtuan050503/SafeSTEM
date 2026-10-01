from datetime import datetime

from sqlalchemy import String, Text, Float, Integer, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from backend.app.database.base import Base


class VerificationAttempt(Base):
    __tablename__ = "verification_attempts"

    attempt_id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True
    )

    assignment_id: Mapped[int] = mapped_column(
        ForeignKey("assignments.assignment_id")
    )

    checkpoint_id: Mapped[int] = mapped_column(
        ForeignKey("checkpoints.checkpoint_id")
    )

    attempt_number: Mapped[int] = mapped_column(
        Integer,
        default=1
    )

    status: Mapped[str] = mapped_column(String(30))

    confidence: Mapped[float | None] = mapped_column(
        Float,
        nullable=True
    )

    feedback: Mapped[str | None] = mapped_column(
        Text,
        nullable=True
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.now
    )