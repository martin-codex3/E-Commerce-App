from pydantic import BaseModel, Field
from datetime import datetime

# for creating a new product
class CreateProductSchema(BaseModel):
    product_title: str
    product_description: str
    product_image: str
    product_price: float
    is_product_available: bool
    product_category: str
    created_at: datetime = Field(default=datetime.date)
    updated_at: datetime = Field(default=datetime.date)


# for getting a product
class ProductSchema(BaseModel):
    product_id: int
    product_title: str
    product_description: str
    product_image: str
    product_price: float
    is_product_available: bool
    product_category: str
    created_at: datetime = Field(default=datetime.date)
    updated_at: datetime = Field(default=datetime.date)


# for updating a product
class UpdateProductSchema(BaseModel):
    product_title: str
    product_description: str
    product_image: str
    product_price: float
    is_product_available: bool
    product_category: str
    created_at: datetime = Field(default=datetime.date)
    updated_at: datetime = Field(default=datetime.date)