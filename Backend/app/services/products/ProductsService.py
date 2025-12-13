from sqlmodel.ext.asyncio.session import AsyncSession
from app.models.products.products_model import ProductModel
from app.schemas.products.ProductsSchema import CreateProductSchema, UpdateProductSchema, ProductsSchema
from sqlmodel import select


class ProductsService:

    async def all_products(self, session: AsyncSession):
        statement = select(ProductModel).order_by(ProductModel.created_at)
        # executing the store data command here
        all_products = await session.exec(statement)
        # we will attempt to return the data here
        return all_products.all()


    async def create_product(self, product_data: CreateProductSchema, session: AsyncSession):
        product_dict = product_data.model_dump()

        new_product = ProductModel(
            **product_dict
        )
        # we have to add the data to the session
        session.add(new_product)
        # then we have to commit the changes here
        await session.commit()
        # then we have to close the session
        await session.close()

        return new_product


    async def show_product(self, product_id: int, session: AsyncSession):
        statement = select(ProductModel).where(ProductModel.product_id == product_id)
        results = await session.exec(statement)
        # we will return the single record here
        return results.first()


    async def update_product(self, product_id: int, product_data: UpdateProductSchema,  session: AsyncSession):
        product_to_update = await self.show_product(product_id, session)

        # we will check if the product is not none here
        if product_to_update is not None:
            updated_product = product_data.model_dump()

            for keys, values in updated_product.items():
                setattr(product_to_update, keys, values)

            await session.commit()

            return product_to_update
        else:
            return None

    async def delete_product(self, product_id: int, session: AsyncSession):
        single_product = await self.show_product(product_id, session)
        if single_product is not None:
            await session.delete(single_product)
            await session.commit()
            return None
        else:
            return None
