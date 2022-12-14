from typing import List

from fastapi.encoders import jsonable_encoder
from sqlalchemy import asc, desc
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.item import Item
from app.schemas.item import ItemCreate, ItemUpdate


class CRUDItem(CRUDBase[Item, ItemCreate, ItemUpdate]):

    def get_filtred_name(
            self ,
            substr : str,
            db: Session,
            desc_ : bool = False 
        ) -> List[Item]:

        f = desc if desc_ == True else asc
        
        response = (
            db.query(Item).filter(Item.name.like(f"{substr}%"))
            .order_by(f(Item.name))
            .all()
        )

        return response
        
    def get_filtred_price(
            self ,
            from_ : str ,
            to : str ,
            db: Session,
            desc_ : bool = False 
        ) -> List[Item]:

        f = desc if desc_ == True else asc
        
        response = (
            db.query(Item)
            .filter(Item.price > from_)
            .filter(Item.price < to) 
            .order_by(f(Item.price))
            .all()
        )
        
        return response

    def get_by(
            self ,
            field: str ,
            db: Session,
            desc : bool = False 
        ) -> List[Item]:

        if field == "name":
            response = db.query(Item).order_by(
                Item.name if desc == False else Item.name.desc()
            ).all()
        elif field == "price":
            response = db.query(Item).order_by(
                Item.price if desc == False else Item.price.desc()
            ).all()
        else:
            raise Exception

        return response

item = CRUDItem(Item)