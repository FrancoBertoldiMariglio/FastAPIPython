from .BaseServiceImp import BaseServiceImplement
from ..Repositories.ProductoRepository import ProductoRepository
from ..Entities import Producto

class ProductoServiceImpl(BaseServiceImplement):

    def __int__(self):
        self.baseRepository = ProductoRepository(table=Producto)
