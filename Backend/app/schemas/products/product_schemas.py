from pydantic import BaseModel, Field
from datetime import datetime

# for fetching all products
class ProductSchema(BaseModel):
    product_id: int
    product_title: str
    product_description: str
    product_category: str
    product_price: float = Field(default=0.0)
    product_image: str
    created_at: datetime = Field(default=datetime.now())
    updated_at: datetime = Field(default=datetime.now())


# for creating a new product
class CreateProductSchema(BaseModel):
    product_title: str
    product_description: str
    product_category: str
    product_price: float = Field(default=0.0)
    product_image: str
    created_at: datetime = Field(default=datetime.now())
    updated_at: datetime = Field(default=datetime.now())


# for updating the product here
class UpdateProductSchema(BaseModel):
    product_title: str
    product_description: str
    product_category: str
    product_price: float = Field(default=0.0)
    product_image: str
    created_at: datetime = Field(default=datetime.now())
    updated_at: datetime = Field(default=datetime.now())
