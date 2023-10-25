from .BaseControllerImp import BaseControllerImplement, router
from fastapi import APIRouter, HTTPException
from ..Services.ProductoServiceImp import ProductoServiceImpl
from typing import List
from ..Models.ProductoModel import ProductoModel


routerProducto = APIRouter()


class ProductoControllerImplement(BaseControllerImplement):

    @routerProducto.get("", response_model=List[ProductoModel])
    def getAll(self):
        try:
            return ProductoServiceImpl.findAll()
        except:
            raise HTTPException(status_code=404, detail="Producto no encontrado")

    @routerProducto.get("/{id}", response_model=ProductoModel)
    def getOne(self, id):
        try:
            return ProductoServiceImpl.findOne(id)
        except:
            raise HTTPException(status_code=404, detail=f"No se encontro ningun registro coincidente con el id {id}")

    @routerProducto.post("", response_model=ProductoModel)
    def save(self, producto):
        try:
            return ProductoServiceImpl.save(producto)
        except:
            raise HTTPException(status_code=404, detail=f"No se pudo guardar el registro en producto")

    @routerProducto.delete("/{id}", response_model=str)
    def delete(self, id):
        try:
            return ProductoServiceImpl.delete(id)
        except:
            raise HTTPException(status_code=404, detail=f"No se pudo eliminar el registro en producto")

    @routerProducto.put("/{id}", response_model=ProductoModel)
    def update(self, producto, id):
        try:
            return ProductoServiceImpl.update(producto, id)
        except:
            raise HTTPException(status_code=404, detail=f"No se pudo actualizar el registro en producto")

