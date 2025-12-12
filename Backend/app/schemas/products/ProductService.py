from sqlalchemy.ext.asyncio.session import AsyncSession
from app.models.products.products_model import ProductModel


class ProductsService:

    async def get_all_products(self, session: AsyncSession):
        pass

    async def create_new_product(self, session: AsyncSession):
        pass

    async def show_product(self, product_id: int, session: AsyncSession):
        pass

    async def update_product(self, product_id: int, session: AsyncSession):
        pass

    async def delete_product(self, product_id: int, session: AsyncSession):
        pass