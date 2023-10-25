from .BaseControllerImp import BaseControllerImplement
from fastapi import APIRouter, HTTPException
from ..Services.RatingServiceImp import RatingServiceImpl
from typing import List
from ..Models.RatingModel import RatingModel
from ..Entities.Rating import Rating

routerRating = APIRouter()


class RatingControllerImplement():

    @routerRating.get("", response_model=List[RatingModel])
    def getAll(self):
        try:
            return RatingServiceImpl.findAll()
        except:
            raise HTTPException(status_code=404, detail="Rating no encontrado")

    @routerRating.get("/{id}", response_model=RatingModel)
    def getOne(self, identificador):
        try:
            return RatingServiceImpl.findOne(identificador)
        except:
            raise HTTPException(status_code=404, detail=f"No se encontro ningun registro coincidente con el id {identificador}")

    @routerRating.post("", response_model=RatingModel)
    def save(self, rating):
        try:
            return RatingServiceImpl.save(rating)
        except:
            raise HTTPException(status_code=404, detail=f"No se pudo guardar el registro en rating")

    @routerRating.delete("/{id}", response_model=str)
    def delete(self, identificador):
        try:
            return RatingServiceImpl.delete(identificador)
        except:
            raise HTTPException(status_code=404, detail=f"No se pudo eliminar el registro en rating")

    @routerRating.put("/{id}", response_model=RatingModel)
    def update(self, rating, identificador):
        try:
            return RatingServiceImpl.update(rating, identificador)
        except:
            raise HTTPException(status_code=404, detail=f"No se pudo actualizar el registro en rating")
