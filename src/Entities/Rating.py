from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Rating(Base):
    __tablename__ = 'Rating'
    id = Column(Integer, primary_key=True)
    rate = Column(Float)
    contador = Column(Integer)

    producto = relationship('Producto', back_populates='Rating')