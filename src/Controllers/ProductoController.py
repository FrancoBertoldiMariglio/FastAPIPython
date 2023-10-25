from .BaseControllerImp import BaseControllerImplement
from fastapi import APIRouter, HTTPException
from ..Services.ProductoServiceImp import ProductoServiceImpl
from typing import List
from ..Models.ProductoModel import ProductoModel
from ..Entities.Producto import Producto


routerProducto = APIRouter()


class ProductoControllerImplement():

    @routerProducto.get("", response_model=List[ProductoModel])
    def getAll(self):
        try:
            return ProductoServiceImpl.findAll()
        except:
            raise HTTPException(status_code=404, detail="Producto no encontrado")

    @routerProducto.get("/{id}", response_model=ProductoModel)
    def getOne(self, identificador):
        try:
            return ProductoServiceImpl.findOne(identificador)
        except:
            raise HTTPException(status_code=404, detail=f"No se encontro ningun registro coincidente con el id {identificador}")

    @routerProducto.post("", response_model=ProductoModel)
    def save(self, producto):
        try:
            return ProductoServiceImpl.save(producto)
        except:
            raise HTTPException(status_code=404, detail=f"No se pudo guardar el registro en producto")

    @routerProducto.delete("/{id}", response_model=str)
    def delete(self, identificador):
        try:
            return ProductoServiceImpl.delete(identificador)
        except:
            raise HTTPException(status_code=404, detail=f"No se pudo eliminar el registro en producto")

    @routerProducto.put("/{id}", response_model=ProductoModel)
    def update(self, producto, identificador):
        try:
            return ProductoServiceImpl.update(producto, identificador)
        except:
            raise HTTPException(status_code=404, detail=f"No se pudo actualizar el registro en producto")

