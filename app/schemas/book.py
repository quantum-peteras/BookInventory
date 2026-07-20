from pydantic import BaseModel, Field, ConfigDict, field_validator
from typing import Optional

class BookBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=255)
    author: str = Field(..., min_length=1, max_length=255)
    number_of_pages: int = Field(..., ge=0, strict=True)

    @field_validator('number_of_pages', mode='before')
    @classmethod
    def validate_number_of_pages(cls, v):
        if isinstance(v, str):
            raise ValueError('number_of_pages must be an integer, not a string')
        if not isinstance(v, int):
            raise ValueError('number_of_pages must be an integer')
        return v

class BookCreate(BookBase):
    pass

class BookUpdate(BaseModel):
    title: Optional[str] = None
    author: Optional[str] = None
    number_of_pages: Optional[int] = Field(default=None, ge=0, strict=True)

    @field_validator('number_of_pages', mode='before')
    @classmethod
    def validate_number_of_pages(cls, v):
        if v is None:
            return v
        if isinstance(v, str):
            raise ValueError('number_of_pages must be an integer, not a string')
        if not isinstance(v, int):
            raise ValueError('number_of_pages must be an integer')
        return v

class BookResponse(BookBase):
    id: int
    model_config = ConfigDict(from_attributes=True)