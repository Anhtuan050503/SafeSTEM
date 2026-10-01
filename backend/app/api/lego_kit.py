from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from backend.app.database.database import get_db
from backend.app.models.lego_kit import LegoKit
from backend.app.schemas.lego_kit import (
    LegoKitCreate,
    LegoKitUpdate,
    LegoKitResponse
)


router = APIRouter(
    prefix="/lego-kits",
    tags=["LEGO Kits"]
)


@router.post("/", response_model=LegoKitResponse, status_code=201)
def create_lego_kit(
    data: LegoKitCreate,
    db: Session = Depends(get_db)
):
    kit = LegoKit(**data.model_dump())

    db.add(kit)
    db.commit()
    db.refresh(kit)

    return kit


@router.get("/", response_model=list[LegoKitResponse])
def get_lego_kits(db: Session = Depends(get_db)):
    return db.scalars(
        select(LegoKit).order_by(LegoKit.kit_id)
    ).all()


@router.get("/{kit_id}", response_model=LegoKitResponse)
def get_lego_kit(
    kit_id: int,
    db: Session = Depends(get_db)
):
    kit = db.get(LegoKit, kit_id)

    if not kit:
        raise HTTPException(
            status_code=404,
            detail="LEGO kit not found"
        )

    return kit


@router.put("/{kit_id}", response_model=LegoKitResponse)
def update_lego_kit(
    kit_id: int,
    data: LegoKitUpdate,
    db: Session = Depends(get_db)
):
    kit = db.get(LegoKit, kit_id)

    if not kit:
        raise HTTPException(
            status_code=404,
            detail="LEGO kit not found"
        )

    for field, value in data.model_dump(exclude_unset=True).items():
        setattr(kit, field, value)

    db.commit()
    db.refresh(kit)

    return kit


@router.delete("/{kit_id}")
def delete_lego_kit(
    kit_id: int,
    db: Session = Depends(get_db)
):
    kit = db.get(LegoKit, kit_id)

    if not kit:
        raise HTTPException(
            status_code=404,
            detail="LEGO kit not found"
        )

    db.delete(kit)
    db.commit()

    return {"message": "LEGO kit deleted successfully"}