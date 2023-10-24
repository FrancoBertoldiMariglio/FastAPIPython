from .BaseControllerImp import BaseControllerImplement
from fastapi import APIRouter

routerProdcto = APIRouter()


class ProductoControllerImplement(BaseControllerImplement):
    dir = 'producto'
