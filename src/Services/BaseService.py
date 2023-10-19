from abc import ABC, abstractmethod
from src.Repositories.BaseRepository import BaseRepository

class BaseService(ABC):

    def __init__(self):
        self.baseRepository = BaseRepository

    @abstractmethod
    def findAll(self):
        pass

    @abstractmethod
    def findOne(self, id):
        pass

    @abstractmethod
    def save(self, entity):
        pass

    @abstractmethod
    def update(self, entity, id):
        pass

    @abstractmethod
    def delete(self, id):
        pass