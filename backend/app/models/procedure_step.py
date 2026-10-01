from sqlalchemy import String, Text, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from backend.app.database.base import Base


class ProcedureStep(Base):
    __tablename__ = "procedure_steps"

    step_id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True
    )

    lesson_id: Mapped[int] = mapped_column(
        ForeignKey("lessons.lesson_id")
    )

    step_number: Mapped[int] = mapped_column(Integer)

    title: Mapped[str] = mapped_column(String(200))

    instruction: Mapped[str] = mapped_column(Text)

    reference_image_url: Mapped[str | None] = mapped_column(
        String(500),
        nullable=True
    )