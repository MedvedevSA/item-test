from re import A
from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()



@router.get("/", response_model=List[schemas.Order])
def read_order(
    db: Session = Depends(deps.get_db),
) -> Any:

    orders = crud.order.get_all(db)

    return orders

@router.post("/", response_model=schemas.Order)
def create_order(
    *,
    db: Session = Depends(deps.get_db),
    order_in: schemas.OrderCreate,
) -> Any:
    """
    Create new order.
    """
    item_price = crud.item.get_id(id=order_in.item_id, db=db).price
    order_in.price = item_price*order_in.amount

    order = crud.order.create(db=db, obj_in=order_in)

    return order


@router.put("/{id}", response_model=schemas.Order)
def update_order(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    order_in: schemas.OrderUpdate,
) -> Any:
    """
    Update an order.
    """

    order = crud.order.get_id(db=db, id=id)
    order_in.item_id = order.item_id
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")

    item_price = crud.item.get_id(id=order_in.item_id, db=db).price
    order_in.price = item_price*order_in.amount

    order = crud.order.update(db=db, db_obj=order, obj_in=order_in)
    return order