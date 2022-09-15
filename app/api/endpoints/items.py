from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()



@router.get("/", response_model=List[schemas.Item])
def read_items(
    sortfield : str = None,
    desc : bool = False,
    db: Session = Depends(deps.get_db),
) -> Any:

    if not sortfield :
        items = crud.item.get_all(db)
    else: 
        items = crud.item.get_by(field=sortfield, desc=desc, db=db)

    return items

@router.get("/name", response_model=List[schemas.Item])
def filtred_name_items(
    substr : str = "",
    desc : bool = False,
    db: Session = Depends(deps.get_db),
) -> Any:

    items = crud.item.get_filtred_name(substr, desc_=desc, db=db)
    if not items:
        raise HTTPException(status_code=404, detail="Item not found")

    return items

@router.get("/price", response_model=List[schemas.Item])
def filtred_price_items(
    from_ : float = None,
    to : float = None,
    desc : bool = False,
    db: Session = Depends(deps.get_db),
) -> Any:

    items = crud.item.get_filtred_price(from_=from_, to=to, desc_=desc, db=db)
    if not items:
        raise HTTPException(status_code=404, detail="Item not found")

    return items

@router.get("/{item_id}", response_model=schemas.Item)
def read_item_id(
    item_id: int ,
    db: Session = Depends(deps.get_db)
) -> Any:


    item_by_id = crud.item.get_id(db, id=item_id)

    if not item_by_id:
        raise HTTPException(status_code=404, detail="Item not found")

    return item_by_id

@router.post("/", response_model=schemas.Item)
def create_item(
    *,
    db: Session = Depends(deps.get_db),
    item_in: schemas.OrderCreate,
) -> Any:
    """
    Create new item.
    """

    item = crud.item.create(db=db, obj_in=item_in)
    
    return item


@router.put("/{id}", response_model=schemas.Item)
def update_item(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    item_in: schemas.ItemUpdate,
) -> Any:
    """
    Update an item.
    """
    item = crud.item.get_id(db=db, id=id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    item = crud.item.update(db=db, db_obj=item, obj_in=item_in)
    return item