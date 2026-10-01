from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from backend.app.database.database import get_db
from backend.app.models.lego_part import LegoPart
from backend.app.schemas.lego_part import (
    LegoPartCreate,
    LegoPartUpdate,
    LegoPartResponse
)


router = APIRouter(
    prefix="/lego-parts",
    tags=["LEGO Parts"]
)


@router.post("/", response_model=LegoPartResponse, status_code=201)
def create_lego_part(
    data: LegoPartCreate,
    db: Session = Depends(get_db)
):
    existing = db.scalar(
        select(LegoPart).where(
            LegoPart.part_code == data.part_code
        )
    )

    if existing:
        raise HTTPException(
            status_code=409,
            detail="Part code already exists"
        )

    part = LegoPart(**data.model_dump())

    db.add(part)
    db.commit()
    db.refresh(part)

    return part


@router.get("/", response_model=list[LegoPartResponse])
def get_lego_parts(db: Session = Depends(get_db)):
    return db.scalars(
        select(LegoPart).order_by(LegoPart.part_id)
    ).all()


@router.get("/{part_id}", response_model=LegoPartResponse)
def get_lego_part(
    part_id: int,
    db: Session = Depends(get_db)
):
    part = db.get(LegoPart, part_id)

    if not part:
        raise HTTPException(
            status_code=404,
            detail="LEGO part not found"
        )

    return part


@router.put("/{part_id}", response_model=LegoPartResponse)
def update_lego_part(
    part_id: int,
    data: LegoPartUpdate,
    db: Session = Depends(get_db)
):
    part = db.get(LegoPart, part_id)

    if not part:
        raise HTTPException(
            status_code=404,
            detail="LEGO part not found"
        )

    update_data = data.model_dump(exclude_unset=True)

    if "part_code" in update_data:
        existing = db.scalar(
            select(LegoPart).where(
                LegoPart.part_code == update_data["part_code"],
                LegoPart.part_id != part_id
            )
        )

        if existing:
            raise HTTPException(
                status_code=409,
                detail="Part code already exists"
            )

    for field, value in update_data.items():
        setattr(part, field, value)

    db.commit()
    db.refresh(part)

    return part


@router.delete("/{part_id}")
def delete_lego_part(
    part_id: int,
    db: Session = Depends(get_db)
):
    part = db.get(LegoPart, part_id)

    if not part:
        raise HTTPException(
            status_code=404,
            detail="LEGO part not found"
        )

    db.delete(part)
    db.commit()

    return {"message": "LEGO part deleted successfully"}