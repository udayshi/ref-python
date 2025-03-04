from sqlalchemy.orm import Session
from . import models, schemas
class ItemRepo:
    def list(self,db: Session, skip: int = 0, limit: int = 10):
        return db.query(models.Item).offset(skip).limit(limit).all()

    def get(self,db: Session, item_id: int):
        return db.query(models.Item).filter(models.Item.id == item_id).first()

    def create(self,db: Session, item: schemas.ItemCreate):
        db_item = models.Item(name=item.name, description=item.description)
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
        return db_item

    def delete(self,db: Session, item_id: int):
        db_item = db.query(models.Item).filter(models.Item.id == item_id).first()
        if db_item:
            db.delete(db_item)
            db.commit()
        return db_item
