from .BaseController import BaseController
from fastapi import APIRouter
from ..Services.BaseServiceImp import BaseServiceImplement as service

router = APIRouter()

class BaseControllerImplement(BaseController):

    dir = 'base'

    @router.get("/" + dir + "/")
    def getAll(self):
        try:
            return service.findAll()
        except:
            return 404, f"Error en la consulta de {dir}"

    @router.get("/" + dir + "/{id}")
    def getOne(self, id):
        try:
            return service.findById(id)
        except:
            return 404, f"No se encontro ningun registro coincidente con el id {id}"

    @router.get("/" + dir + "/{pages}")
    def getAllPageable(self, pages):
        try:
            return service.findAllPageable(pages)
        except:
            return 404, f"Error en la consulta de {dir}"

    @router.post("/" + dir + "/")
    def save(self, object):
        try:
            return service.save(object)
        except:
            return 404, f"No se pudo guardar el registro en {dir}"

    @router.put("/" + dir + "/{id}")
    def update(self, object, id):
        try:
            return service.update(object, id)
        except:
            return 404, f"No se pudo actualizar el registro en {dir}"

    @router.delete("/" + dir + "/{id}")
    def delete(self, id):
        try:
            return service.delete(id)
        except:
            return 404, f"No se pudo eliminar el registro en {dir}"
