from sqlalchemy import String, Text, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from backend.app.database.base import Base


class VerificationError(Base):
    __tablename__ = "verification_errors"

    error_id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True
    )

    attempt_id: Mapped[int] = mapped_column(
        ForeignKey("verification_attempts.attempt_id")
    )

    model_part_id: Mapped[int | None] = mapped_column(
        ForeignKey("model_parts.model_part_id"),
        nullable=True
    )

    error_type: Mapped[str] = mapped_column(String(50))

    description: Mapped[str | None] = mapped_column(
        Text,
        nullable=True
    )

    suggestion: Mapped[str | None] = mapped_column(
        Text,
        nullable=True
    )