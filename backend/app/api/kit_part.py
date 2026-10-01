from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from backend.app.database.database import get_db
from backend.app.models.lego_kit import LegoKit
from backend.app.models.lego_part import LegoPart
from backend.app.models.kit_part import KitPart
from backend.app.schemas.kit_part import (
    KitPartCreate,
    KitPartResponse
)


router = APIRouter(
    prefix="/lego-kits",
    tags=["Kit Parts"]
)


@router.post(
    "/{kit_id}/parts",
    response_model=KitPartResponse,
    status_code=201
)
def add_part_to_kit(
    kit_id: int,
    data: KitPartCreate,
    db: Session = Depends(get_db)
):
    if data.quantity <= 0:
        raise HTTPException(
            status_code=400,
            detail="Quantity must be greater than 0"
        )

    kit = db.get(LegoKit, kit_id)

    if not kit:
        raise HTTPException(
            status_code=404,
            detail="LEGO kit not found"
        )

    part = db.get(LegoPart, data.part_id)

    if not part:
        raise HTTPException(
            status_code=404,
            detail="LEGO part not found"
        )

    existing = db.scalar(
        select(KitPart).where(
            KitPart.kit_id == kit_id,
            KitPart.part_id == data.part_id
        )
    )

    if existing:
        raise HTTPException(
            status_code=409,
            detail="Part already exists in this kit"
        )

    kit_part = KitPart(
        kit_id=kit_id,
        part_id=data.part_id,
        quantity=data.quantity
    )

    db.add(kit_part)
    db.commit()
    db.refresh(kit_part)

    return kit_part


@router.get(
    "/{kit_id}/parts",
    response_model=list[KitPartResponse]
)
def get_kit_parts(
    kit_id: int,
    db: Session = Depends(get_db)
):
    kit = db.get(LegoKit, kit_id)

    if not kit:
        raise HTTPException(
            status_code=404,
            detail="LEGO kit not found"
        )

    return db.scalars(
        select(KitPart).where(
            KitPart.kit_id == kit_id
        )
    ).all()


@router.delete("/{kit_id}/parts/{part_id}")
def remove_part_from_kit(
    kit_id: int,
    part_id: int,
    db: Session = Depends(get_db)
):
    kit_part = db.get(
        KitPart,
        (kit_id, part_id)
    )

    if not kit_part:
        raise HTTPException(
            status_code=404,
            detail="Part is not in this kit"
        )

    db.delete(kit_part)
    db.commit()

    return {"message": "Part removed from kit successfully"}