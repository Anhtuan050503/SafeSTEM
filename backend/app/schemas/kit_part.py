from pydantic import BaseModel, ConfigDict


class KitPartCreate(BaseModel):
    part_id: int
    quantity: int


class KitPartResponse(BaseModel):
    kit_id: int
    part_id: int
    quantity: int

    model_config = ConfigDict(from_attributes=True)