from sqlalchemy.orm import Mapped, mapped_column

from src.db import Base


class Product (Base):
    __tablename__ = 'PRODUCT'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    price: Mapped[str]
    image: Mapped[str]
