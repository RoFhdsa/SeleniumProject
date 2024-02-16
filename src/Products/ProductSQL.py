from src.Products.models_product import Product
from src.db import session_bd
from sqlalchemy import select
class ProductSQL:

    @staticmethod
    def insert_data(datas):
        with session_bd() as session:
            for id, product in datas.items():
                row = Product(
                    name=product['name'],
                    price=product['price'],
                    image=product['image'])
                session.add(row)
            session.commit()

    @staticmethod
    def get_product():
        with session_bd() as session:
            query = (
                select(Product.id, Product.name, Product.price, Product.image).select_from(Product)
            )
            result = session.execute(query)
            result =  result.fetchall()
            print(f' result = {result}')
            product_data=[]
            for row in result:
                product_dict = {
                    "name":row.name,
                    "price":row.price,
                    "image":row.image
                }
                product_data.append(product_dict)
            print(f'product_data = {product_data}')
            return product_data