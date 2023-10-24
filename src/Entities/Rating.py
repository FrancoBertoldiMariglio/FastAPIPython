from sqlalchemy.orm import relationship
from .Base import Base
from sqlalchemy import Column, Integer, String, Float, ForeignKey


class Rating(Base):
    __tablename__ = 'Rating'
    rate = Column(Float)
    contador = Column(Integer)

    producto = relationship('Producto', back_populates='Rating')