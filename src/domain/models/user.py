from pydantic import BaseModel, Field


class User(BaseModel):
    id: str | None = Field(default=None, alias="_id")
    name: str
    email: str

    class Config:
        populate_by_name = True
