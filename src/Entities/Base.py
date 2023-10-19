from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
Base = declarative_base()


class Base(Base):
    id = Column(Integer, primary_key = True)