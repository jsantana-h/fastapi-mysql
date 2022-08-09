from sqlalchemy import Table, Column, Integer, String, DateTime
from conf.db import meta, engine

User = Table('user', meta, Column('id', Integer, primary_key=True),
             Column('name', String(50)),
             Column('email', String(250)),
             Column('password', String(250)),
             Column('created_at', DateTime),
             Column('updated_at', DateTime))

meta.create_all(engine)
