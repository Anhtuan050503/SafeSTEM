from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from backend.app.database.base import Base


class KitPart(Base):
    __tablename__ = "kit_parts"

    kit_id: Mapped[int] = mapped_column(
        ForeignKey("lego_kits.kit_id"),
        primary_key=True
    )

    part_id: Mapped[int] = mapped_column(
        ForeignKey("lego_parts.part_id"),
        primary_key=True
    )

    quantity: Mapped[int] = mapped_column(default=1)