from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.Order])
def read_items_filter_by(
    filter_by : str,
    sort_by : str,
    db: Session = Depends(deps.get_db),
) -> Any:

    orders = crud.order.get_all(db)

    return orders

@router.get("/", response_model=List[schemas.Order])
def read_items(
    db: Session = Depends(deps.get_db),
) -> Any:

    orders = crud.order.get_all(db)

    return orders

@router.post("/", response_model=schemas.Order)
def create_order(
    *,
    db: Session = Depends(deps.get_db),
    item_in: schemas.OrderCreate,
) -> Any:
    """
    Create new item.
    """
    order = crud.order.create(db=db, obj_in=item_in)
    return order