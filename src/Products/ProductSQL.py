from src.Products.models_product import Product
from src.db import session_bd


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
