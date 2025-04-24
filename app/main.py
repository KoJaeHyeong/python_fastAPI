from enum import Enum
from turtle import st
from fastapi import FastAPI, Query
from pydantic import BaseModel

from auto_commit import git_auto_push

class CharacterName(str,Enum):
    captain =  'captain'
    spider_man = 'spider_man'

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


app = FastAPI(
    title="FastAPI Project",
    description="FastAPI 프로젝트",
    version="1.0.0"
)



@app.get("/")
async def root():
    return {"message": "Welcome to FastAPI"}

# @app.get("/items/{id}")
# async def getItems(id: int):
#     return {"age": id + 1}

@app.get('/marvels/{character_name}')
async def getMarvelsWeapons(character_name: CharacterName):
    if character_name is CharacterName.captain:        
        return {'weapon': '방패'}
    
    if character_name is CharacterName.spider_man:        
        return {'weapon': '거미줄'}
    
@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

class Pagination(BaseModel) :
    skip: int;
    limit: int;

@app.get('/query')
# async def get_query(skip: int = 0, limit: int = 10):
async def get_query(req_dto: Pagination = Query(...)):
    # return fake_items_db[skip: skip + limit]
    return fake_items_db[req_dto.skip: req_dto.skip + req_dto.limit]

@app.get('/query/{query_id}')
async def get_query2(id: str, q: str | None = None):
    if q:
        return {"id": id, "q": q}
    return {"id": id, "q": None}

@app.get("/items/{item_id}")
async def read_item(item_id: str, q: str | None = None, short: bool = False):
    item = {"item_id": item_id}
    if q:
        item["b"] = "sdsd"
        item.update({'sd':"dd"})
        item.update({"q": q})
        print(item)
    if not short:
        print(short)
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item


@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(
    user_id: int, item_id: str, q: str | None = None, short: bool = False
):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item

@app.post("/items/")
async def create_item(item: Item):
    item_dict = vars(item)
    print(item_dict)
    if item.tax is not None:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item) :
    result = {"item_id": item_id, **vars(item)}

    # if q:
    #     result.update({"q": q})

    return result

git_auto_push('fast_api 공부')