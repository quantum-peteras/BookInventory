from pydantic import BaseModel, Field, ConfigDict
from typing import Optional

class BookBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=255)
    author: str = Field(..., min_length=1, max_length=255)
    number_of_pages: int = Field(..., ge=0)

class BookCreate(BookBase):
    pass

class BookUpdate(BaseModel):
    title: Optional[str] = None
    author: Optional[str] = None
    number_of_pages: Optional[int] = Field(default=None, ge=0)

class BookResponse(BookBase):
    id: int
    model_config = ConfigDict(from_attributes=True)