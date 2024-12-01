from fastapi import APIRouter, HTTPException
from typing import List, Optional
from .models import Item

router = APIRouter()

# In-memory storage (simulate a database)
items_db = []
item_id_counter = 0

@router.post("/items/", response_model=Item, status_code=201)
def create_item(item: Item):
    global item_id_counter
    item_id_counter += 1
    item.id = item_id_counter
    items_db.append(item)
    return item

@router.get("/items/", response_model=List[Item])
def list_items(skip: int = 0, limit: Optional[int] = None):
    return items_db[skip:skip + (limit or len(items_db))]

@router.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int):
    for item in items_db:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")

@router.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, updated_item: Item):
    for index, item in enumerate(items_db):
        if item.id == item_id:
            updated_item.id = item_id
            items_db[index] = updated_item
            return updated_item
    raise HTTPException(status_code=404, detail="Item not found")

@router.delete("/items/{item_id}", status_code=204)
def delete_item(item_id: int):
    for index, item in enumerate(items_db):
        if item.id == item_id:
            del items_db[index]
            return
    raise HTTPException(status_code=404, detail="Item not found")
