from sqlmodel.ext.asyncio.session import AsyncSession
from ...models.products.product_model import ProductModel
from ...schemas.products.product_schemas import CreateProductSchema, ProductSchema, UpdateProductSchema
from sqlmodel import select, desc


class ProductService:

    async def all_products(self, session: AsyncSession):
        statement = select(ProductModel).order_by(desc(ProductModel.created_at))
        # fetching all products here
        results = await session.exec(statement)
        return results.all()

    async def show_product(self, product_id: int, session: AsyncSession):
        statement = select(ProductModel).where(ProductModel.product_id == product_id)
        results = await session.exec(statement)
        return results.first()

    async def create_product(self, product_data: CreateProductSchema, session: AsyncSession):
        product_data_dict = product_data.model_dump()
        # filling the model with the incoming data
        new_product_data = ProductModel(**product_data_dict)
        # adding the data to the session
        session.add(new_product_data)
        # commiting the changes
        await session.commit()

        return new_product_data


    async def update_product(self, product_id: int, product_data: UpdateProductSchema, session: AsyncSession):
        product_to_update = await self.show_product(product_id = product_id, session = session)

        if product_to_update is not None:

            product_data_dict = product_data.model_dump()
            for keys, values in product_data_dict.items():
                setattr(product_to_update, keys, values)


            # we will add the product to the session
            session.add(product_to_update)
            await session.commit()
            return product_to_update

        else:
            return None


    async def delete_product(self, product_id: int, session: AsyncSession):
        product_to_delete = await self.show_product(product_id = product_id, session = session)

        if product_to_delete is not None:
            await session.delete(product_to_delete)
            await session.commit()
            return None
        else:
            return None
