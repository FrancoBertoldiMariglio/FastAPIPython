from .BaseService import BaseService
from ..Repositories.BaseRepository import BaseRepository
from ..Entities import Base


class BaseServiceImplement(BaseService):

    def __int__(self):
        self.baseRepository = BaseRepository(table=Base)

    def findAll(self):
        try:
            return self.baseRepository.findAll()
        except Exception as e:
            raise Exception(str(e))

    def findOne(self, identificador):
        try:
            return self.baseRepository.findById(identificador)
        except Exception as e:
            raise Exception(str(e))

    def save(self, entity):
        try:
            return self.baseRepository.save(entity)
        except Exception as e:
            raise Exception(str(e))

    def update(self, entity, identificador):
        try:
            optEntity = self.baseRepository.findById(identificador)
            if optEntity:
                entityUpdate = self.baseRepository.save(entity)
                return entityUpdate
        except Exception as e:
            raise Exception(str(e))

    def delete(self, identificador):
        try:
            if self.baseRepository.findById(identificador):
                self.baseRepository.delete(identificador)
                return True
            else:
                raise Exception()
        except Exception as e:
            raise Exception(str(e))
