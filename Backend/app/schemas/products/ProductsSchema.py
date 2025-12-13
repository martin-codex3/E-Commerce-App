from pydantic import Field, BaseModel
from datetime import datetime

# for fetching all products
class ProductsSchema(BaseModel):
    product_id: int = Field(default=None)
    product_title: str = Field(default=None)
    product_description: str
    product_category: str
    product_price: str
    product_image: str
    created_ate: datetime = Field(default=datetime.now())
    updated_at: datetime = Field(default=datetime.now())


# for creating a new product
class CreateProductSchema(BaseModel):
    product_title: str = Field(default=None)
    product_description: str
    product_category: str
    product_price: str
    product_image: str
    created_ate: datetime = Field(default=datetime.now())
    updated_at: datetime = Field(default=datetime.now())


# for updating the product
class UpdateProductSchema(BaseModel):
    product_title: str = Field(default=None)
    product_description: str
    product_category: str
    product_price: str
    product_image: str
    created_at: datetime = Field(default=datetime.now())
    updated_at: datetime = Field(default=datetime.now())
