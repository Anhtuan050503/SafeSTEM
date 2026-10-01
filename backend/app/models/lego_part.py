from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from backend.app.database.base import Base


class LegoPart(Base):
    __tablename__ = "lego_parts"

    part_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    part_code: Mapped[str] = mapped_column(
        String(50),
        unique=True,
        index=True
    )

    name: Mapped[str] = mapped_column(String(100))

    category: Mapped[str | None] = mapped_column(
        String(50),
        nullable=True
    )

    model_url: Mapped[str | None] = mapped_column(
        String(500),
        nullable=True
    )