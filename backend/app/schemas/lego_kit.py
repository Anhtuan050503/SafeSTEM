from pydantic import BaseModel, ConfigDict


class LegoKitCreate(BaseModel):
    name: str
    description: str | None = None
    is_supported: bool = True


class LegoKitUpdate(BaseModel):
    name: str | None = None
    description: str | None = None
    is_supported: bool | None = None


class LegoKitResponse(BaseModel):
    kit_id: int
    name: str
    description: str | None
    is_supported: bool

    model_config = ConfigDict(from_attributes=True)