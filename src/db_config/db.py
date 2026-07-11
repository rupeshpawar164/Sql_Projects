import asyncio

from sqlalchemy.ext.asyncio import create_async_engine,async_sessionmaker
from sqlalchemy.orm import DeclarativeBase

DB_URL= "mysql+aiomysql://root:rupesh%40123@localhost/hospital_mangment_sqlalchemy"
engine=create_async_engine(DB_URL,echo=True)
sessionLocal=async_sessionmaker(bind=engine)
class Base(DeclarativeBase):
    pass

if sessionLocal:
    print("connected")
else:
    print('not connected')




