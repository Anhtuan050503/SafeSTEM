from pydantic import BaseModel, ConfigDict


class LegoPartCreate(BaseModel):
    part_code: str
    name: str
    category: str | None = None
    model_url: str | None = None


class LegoPartUpdate(BaseModel):
    part_code: str | None = None
    name: str | None = None
    category: str | None = None
    model_url: str | None = None


class LegoPartResponse(BaseModel):
    part_id: int
    part_code: str
    name: str
    category: str | None
    model_url: str | None

    model_config = ConfigDict(from_attributes=True)