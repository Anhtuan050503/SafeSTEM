from sqlalchemy import String, Text, Boolean
from sqlalchemy.orm import Mapped, mapped_column

from backend.app.database.base import Base


class LegoKit(Base):
    __tablename__ = "lego_kits"

    kit_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    name: Mapped[str] = mapped_column(String(100))
    description: Mapped[str | None] = mapped_column(Text, nullable=True)

    is_supported: Mapped[bool] = mapped_column(Boolean, default=True)