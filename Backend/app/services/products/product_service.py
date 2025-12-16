from sqlmodel.ext.asyncio.session import AsyncSession
from app.schemas.products.product_schemas import CreateProductSchema, ProductSchema, UpdateProductSchema
from sqlmodel import select, desc
from app.models.products.product_model import ProductModel


class ProductService:

    async def get_all_products(self, session: AsyncSession):
        statement = select(ProductModel).order_by(desc(ProductModel.created_at))
        results = await session.exec(statement)

        return results.all()


    async def show_single_product(self, session: AsyncSession, product_id: int):
        statement = select(ProductModel).where(ProductModel.product_id == product_id)
        results = await session.exec(statement)

        return results.first()


    async def create_new_product(self, product_data: CreateProductSchema, session: AsyncSession):
        product = product_data.model_dump()
        new_product = ProductModel(**product)

        if new_product is not None:
            session.add(new_product)
            await session.commit()
            return new_product
        else:
            return None


    async def update_product(self, product_id: int, product_data: UpdateProductSchema, session: AsyncSession):
        product_to_update = await self.show_single_product(session = session, product_id = product_id)

        if product_to_update is not None:
            product_to_update_dict = product_data.model_dump()

            for keys, values in product_to_update_dict.items():
                setattr(product_to_update, keys, values)

            session.add(product_to_update)
            await session.commit()

            return product_to_update
        else:
            return None


    async def delete_product(self, product_id: int, session: AsyncSession):
        product = await self.show_single_product(product_id = product_id, session = session)

        if product is not None:
            await session.delete(product)
            await session.commit()
            return None
        else:
            return None






