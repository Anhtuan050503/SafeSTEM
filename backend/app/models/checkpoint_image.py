from datetime import datetime

from sqlalchemy import String, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from backend.app.database.base import Base


class CheckpointImage(Base):
    __tablename__ = "checkpoint_images"

    image_id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True
    )

    attempt_id: Mapped[int] = mapped_column(
        ForeignKey("verification_attempts.attempt_id")
    )

    image_url: Mapped[str] = mapped_column(String(500))

    view_type: Mapped[str | None] = mapped_column(
        String(30),
        nullable=True
    )

    captured_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.now
    )