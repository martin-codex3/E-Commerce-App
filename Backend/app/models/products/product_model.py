import datetime

from sqlmodel import SQLModel, Field
from datetime import datetime


class ProductModel(SQLModel, table = True):

    __tablename__ = "products"

    product_id: int = Field(default=None, primary_key=True)
    product_title: str = Field(default=None, index=True)
    product_description: str = Field(default=None, index=True)
    product_image: str = Field(default=None)
    product_price: float = Field(default=0.0)
    is_product_available: bool = Field(default=False)
    product_category: str = Field(default=None)
    created_at: datetime.date = Field(default=datetime.date)
    updated_at: datetime.date = Field(default=datetime.date)
