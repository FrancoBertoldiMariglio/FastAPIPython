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

    def findOne(self, id):
        try:
            return self.baseRepository.findById(id)
        except Exception as e:
            raise Exception(str(e))

    def save(self, entity):
        try:
            return self.baseRepository.save(entity)
        except Exception as e:
            raise Exception(str(e))

    def update(self, entity, id):
        try:
            optEntity = self.baseRepository.findById(id)
            if optEntity != None:
                entityUpdate = self.baseRepository.save(entity)
                return entityUpdate
        except Exception as e:
            raise Exception(str(e))

    def delete(self, id):
        try:
            if self.baseRepository.findById(id) != None:
                self.baseRepository.delete(id)
                return True
            else:
                raise Exception()
        except Exception as e:
            raise Exception(str(e))
