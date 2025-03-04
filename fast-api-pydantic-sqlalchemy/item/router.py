from fastapi import APIRouter,Depends, HTTPException 
from sqlalchemy.orm import Session
from . import   schemas,item_repo as crud
from auth.main import get_current_active_user


from db import engine, Base, get_db

# Initialize database
Base.metadata.create_all(bind=engine)
rtr=APIRouter()




@rtr.post("/items/", response_model=schemas.Item)
async def create_item(item: schemas.ItemCreate, db: Session = Depends(get_db), User = Depends(get_current_active_user)):
    return crud.create(db=db, item=item)

@rtr.get("/items/", response_model=list[schemas.Item])
async def read_items(skip: int = 0, limit: int = 10, db: Session = Depends(get_db), User = Depends(get_current_active_user)):
    return crud.list(db=db, skip=skip, limit=limit)

@rtr.get("/items/{item_id}", response_model=schemas.Item)
async def read_item(item_id: int, db: Session = Depends(get_db), User = Depends(get_current_active_user)):
    db_item = crud.get(db=db, item_id=item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item

@rtr.delete("/items/{item_id}")
async def delete_item(item_id: int, db: Session = Depends(get_db), User = Depends(get_current_active_user)):
    db_item = crud.delete(db=db, item_id=item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"message": "Item deleted successfully"}