from pydantic import BaseModel, HttpUrl
from datetime import datetime

class LinkCreate(BaseModel):
    url: HttpUrl
    title: str
    description: str | None = None
    tags: str | None = None

class LinkResponse(BaseModel):
    id: int
    url: str
    title: str
    description: str | None
    tags: str | None
    created_at: datetime

    model_config = {"from_attributes": True}