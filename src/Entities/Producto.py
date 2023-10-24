from sqlalchemy.orm import relationship
from .Base import Base
from sqlalchemy import Column, Integer, String, Float, ForeignKey


class Producto(Base):
    __tablename__ = 'Producto'
    titulo = Column(String)
    precio_compra = Column(Float)
    descripcion = Column(String)
    categoria = Column(String)
    imagen = Column(String)
    rating_id = Column(Integer, ForeignKey('Rating.id'))

    rating = relationship('Rating', back_populates='Producto')
