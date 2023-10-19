from .BaseServiceImp import BaseServiceImplement
from ..Repositories.RatingRepository import RatingRepository
from ..Entities import Rating

class ProductoServiceImpl(BaseServiceImplement):

    def __int__(self):
        self.baseRepository = RatingRepository(table=Rating)
