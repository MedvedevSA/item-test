from typing import Optional

from pydantic import BaseModel


# Shared properties
class OrderBase(BaseModel):
    item_id: int
    amount: int

# Properties to receive on item creation
class OrderCreate(OrderBase):
    price : Optional[float] = None

# Properties to receive on item update
class OrderUpdate(OrderBase):
    price : Optional[float] = None


# Properties shared by models stored in DB
class OrderInDBBase(OrderBase):
    id: int
    item_id: int
    amount: int
    price : Optional[float] = None

    class Config:
        orm_mode = True


# Properties to return to client
class Order(OrderInDBBase):
    pass


# Properties properties stored in DB
class OrderInDB(OrderInDBBase):
    pass