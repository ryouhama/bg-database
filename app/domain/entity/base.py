from pydantic import BaseModel, ConfigDict
from app.domain.value_object.base import PrimaryKey


class Entity(BaseModel):
    model_config = ConfigDict(strict=True)
    id: PrimaryKey
