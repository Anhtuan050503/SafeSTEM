from sqlalchemy import String, Integer, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from backend.app.database.base import Base


class Checkpoint(Base):
    __tablename__ = "checkpoints"

    checkpoint_id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True
    )

    lesson_id: Mapped[int] = mapped_column(
        ForeignKey("lessons.lesson_id")
    )

    after_step_id: Mapped[int] = mapped_column(
        ForeignKey("procedure_steps.step_id")
    )

    name: Mapped[str] = mapped_column(String(200))

    checkpoint_order: Mapped[int] = mapped_column(Integer)

    is_final: Mapped[bool] = mapped_column(
        Boolean,
        default=False
    )