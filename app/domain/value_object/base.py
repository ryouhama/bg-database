from uuid import UUID

from pydantic import BaseModel, ConfigDict, model_serializer


class ValueObject(BaseModel):
    model_config = ConfigDict(frozen=True, strict=True)
    pass


class PrimaryKey(ValueObject):
    value: int

    @classmethod
    def generate(cls, value: int) -> "PrimaryKey":
        return cls(value=value)

    @model_serializer
    def serialize(self) -> int:
        return self.value

    def __repr__(self) -> str:
        return self.value.__repr__()

    def __eq__(self, __value: object) -> bool:
        if not isinstance(__value, PrimaryKey):
            return False
        return self.value.__eq__(__value.value)


class PrimaryUUID(PrimaryKey):
    value: UUID

    @classmethod
    def generate(cls, value: UUID) -> "PrimaryUUID":
        return cls(value=value)

    @classmethod
    def generate(cls, value: str) -> "PrimaryUUID":
        return cls(value=UUID(value))

    @model_serializer
    def serialize(self) -> UUID:
        return self.value

    def __repr__(self) -> str:
        return self.value.__repr__()

    def __eq__(self, __value: object) -> bool:
        if not isinstance(__value, PrimaryUUID):
            return False
        return self.value.__eq__(__value.value)
