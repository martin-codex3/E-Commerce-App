from sqlmodel import SQLModel, Field
from datetime import datetime

class CategoryModel(SQLModel, table = True):

    __tablename__ = "categories"

    category_id: int = Field(default=None, primary_key=True)
    category_title: str = Field(default=None, index=True)
    category_description: str = Field(default=None, index=True)
    created_at: datetime = Field(default=datetime.date)
    updated_at: datetime = Field(default=datetime.date)
    
