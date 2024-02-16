from sqlalchemy import create_engine, String
from sqlalchemy.orm import sessionmaker, Session, DeclarativeBase
from sqlalchemy.sql.annotation import Annotated
from DATA.data_test import URL, BD

syns_engine = create_engine(
    url=BD.path_bd_origin,
    echo=True
)

session_bd = sessionmaker(syns_engine)
print(session_bd)

class Base(DeclarativeBase):
    pass
