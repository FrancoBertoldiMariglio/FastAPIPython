from .BaseControllerImp import BaseControllerImplement, router
from fastapi import APIRouter, HTTPException
from ..Services.RatingServiceImp import ProductoServiceImpl
from typing import List
from ..Models.RatingModel import RatingModel

routerRating = APIRouter()


class ProductoControllerImplement(BaseControllerImplement):

    @routerRating.get("", response_model=List[RatingModel])
    def getAll(self):
        try:
            return ProductoServiceImpl.findAll()
        except:
            raise HTTPException(status_code=404, detail="Rating no encontrado")

    @routerRating.get("/{id}", response_model=RatingModel)
    def getOne(self, id):
        try:
            return ProductoServiceImpl.findOne(id)
        except:
            raise HTTPException(status_code=404, detail=f"No se encontro ningun registro coincidente con el id {id}")

    @routerRating.post("", response_model=RatingModel)
    def save(self, raiting):
        try:
            return ProductoServiceImpl.save(raiting)
        except:
            raise HTTPException(status_code=404, detail=f"No se pudo guardar el registro en raiting")

    @routerRating.delete("/{id}", response_model=str)
    def delete(self, id):
        try:
            return ProductoServiceImpl.delete(id)
        except:
            raise HTTPException(status_code=404, detail=f"No se pudo eliminar el registro en raiting")

    @routerRating.put("/{id}", response_model=RatingModel)
    def update(self, raiting, id):
        try:
            return ProductoServiceImpl.update(raiting, id)
        except:
            raise HTTPException(status_code=404, detail=f"No se pudo actualizar el registro en raiting")
