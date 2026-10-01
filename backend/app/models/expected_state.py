from sqlalchemy import Float, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from backend.app.database.base import Base


class ExpectedState(Base):
    __tablename__ = "expected_states"

    expected_state_id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True
    )

    checkpoint_id: Mapped[int] = mapped_column(
        ForeignKey("checkpoints.checkpoint_id")
    )

    model_part_id: Mapped[int] = mapped_column(
        ForeignKey("model_parts.model_part_id")
    )

    expected_position_x: Mapped[float] = mapped_column(Float)
    expected_position_y: Mapped[float] = mapped_column(Float)
    expected_position_z: Mapped[float] = mapped_column(Float)

    expected_rotation_x: Mapped[float] = mapped_column(Float)
    expected_rotation_y: Mapped[float] = mapped_column(Float)
    expected_rotation_z: Mapped[float] = mapped_column(Float)

    is_required: Mapped[bool] = mapped_column(
        Boolean,
        default=True
    )