from sqlmodel.ext.asyncio.session import AsyncSession
from app.schemas.products.product_schemas import CreateProductSchema, ProductSchema, UpdateProductSchema
from sqlmodel import select, desc
from app.models.products.product_model import ProductModel


class ProductService:

    async def get_all_products(self, session: AsyncSession):
        statement = select(ProductModel).order_by(desc(ProductModel.created_at))
        results = await session.exec(statement)

        return results.all()
