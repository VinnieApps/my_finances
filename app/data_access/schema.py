from sqlalchemy import Column, Date, Integer, Numeric, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False)
    password = Column(String(150), nullable=False)

class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, nullable=False, primary_key=True)
    name = Column(String(100), nullable=False)
    user_id = Column(Integer, nullable=False)

class Account(Base):
    __tablename__ = 'accounts'

    id = Column(Integer, nullable=False, primary_key=True)
    name = Column(String(100))
    user_id = Column(Integer, nullable=False)
    type = Column(String(100))

class Preference(Base):
    __tablename__ = 'preferences'

    user_id = Column(Integer, nullable=False, primary_key=True)
    preference = Column(String(60), nullable=False)

class Transaction(Base):
    __tablename__ = 'transactions'

    id = Column(Integer, nullable=False, primary_key=True)
    description = Column(String(150))
    user_id = Column(Integer, nullable=False)
    category_id = Column(Integer)
    date = Column(Date, nullable=False)
    value = Column(Numeric, nullable=False)
    source_accnt_id = Column(Integer, nullable=False)
    link_id = Column(String(150))
