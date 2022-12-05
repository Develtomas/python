from fastapi import FastAPI, Query, Path, Body
import schema
from typing import List

api = FastAPI()


@api.get('/')
def index():
    return {"key": "value"}


@api.get('/{pk}')
def get_item(pk: int, q: float = None):
    return {"key": pk, "q": q}


@api.get('/user/{pk}/items/{item}')
def get_user_item(pk: int, item: str):
    return {"user": pk, "item": item}


@api.get('/book/')
def get_book(q: List[str] = Query("test")):
    return q


@api.get('/book/{pk}')
def get_single_book(pk: int = Path(..., gt=1), pages: int = Query(None, gt=5, le=10)):
    return {"pk": pk, "pages": pages if pages else None}


# @api.post('/book/create/', response_model=schema.Book)
# def create_book(item: schema.Book, author: schema.Author, quantity: int = Body(...)):
#     return {"item": item, "author": author, "quant": quantity}


# @api.post('/book/create/', response_model=schema.Book, response_model_include={"duration", "pages", "genres"})
# def create_book(item: schema.Book):
#     return item


@api.post('/book/create/', response_model=schema.BookOut)
def create_book(item: schema.Book):
    print(item.dict())
    return schema.BookOut(**item.dict(), id=3)


@api.post('/author/create/')
def create_author(author: schema.Author = Body(..., embed=True)):
    return {"author": author}

