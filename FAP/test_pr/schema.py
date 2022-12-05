from pydantic import BaseModel, validator, Field
from datetime import date
from typing import List


class Genre(BaseModel):
    name: str


class Book(BaseModel):
    title: str
    writer: str
    duration: str
    date: date
    summary: str
    genres: List[Genre]
    pages: int = 10


class BookOut(Book):
    id: int


class Author(BaseModel):
    f_name: str
    l_name: str
    age: int = Field(
        ...,
        gt=15,
        le=95,
        description="author have to be between 15 and 95 age"
    )

    # @validator('age')
    # def check_age(cls, v):
    #     if v < 15:
    #         raise ValueError('Error: too young author, need to be older than 15!')
    #     return vs
