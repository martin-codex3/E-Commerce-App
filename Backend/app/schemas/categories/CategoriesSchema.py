from pydantic import BaseModel, Field
from datetime import datetime

# for all the categories
class AllCategorySchema(BaseModel):
    category_id: int = Field(default=None)
    category_title: str = Field(default=None)
    category_description: str = Field(default=None)
    created_at: datetime = Field(default=datetime.date)
    updated_at: datetime = Field(default=datetime.date)


# for creating a new product here
class CreateCategorySchema(BaseModel):
    category_title: str = Field(default=None)
    category_description: str = Field(default=None)
    created_at: datetime = Field(default=datetime.date)
    updated_at: datetime = Field(default=datetime.date)


# for updating a product
class UpdateCategorySchema(BaseModel):
    category_title: str = Field(default=None)
    category_description: str = Field(default=None)
    created_at: datetime = Field(default=datetime.date)
    updated_at: datetime = Field(default=datetime.date)
