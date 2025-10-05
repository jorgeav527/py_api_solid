from pydantic import BaseModel, Field
from bson import ObjectId


class PyObjectId(ObjectId):
    """Custom BSON ObjectId serializer for Pydantic"""

    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid ObjectId")
        return ObjectId(v)


class User(BaseModel):
    id: PyObjectId | None = Field(default=None, alias="_id")
    name: str
    email: str

    class Config:
        json_encoders = {ObjectId: str}
        populate_by_name = True
