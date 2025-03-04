from .item_repo import ItemRepo
from db import engine, Base, get_db

Base.metadata.create_all(bind=engine)
item_repo=ItemRepo()