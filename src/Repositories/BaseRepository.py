from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

class BaseRepository:
    _instance = None

    # Singleton para usar siempre la misma instancia
    def __new__(cls, table):
        if cls._instance is None:
            cls._instance = super(BaseRepository, cls).__new__(cls)
            cls._instance.__init__(table)
        return  cls._instance

    def __init__(self, table):
        self.engine = create_engine('sqlite:///./database.db')
        self.Session = sessionmaker(bind=self.engine)
        self.conn = self.Session()
        self.table = table

    def save(self, objeto):
        try:
            self.conn.add(objeto)
            self.conn.commit()
            return objeto
        except Exception as e:
            raise Exception(str(e))

    def findById(self, identificador):
        try:
            objeto = self.conn.query(self.table).get(identificador)
            self.conn.commit()
            return objeto
        except Exception as e:
            raise Exception(str(e))

    def update(self, objeto):
        try:
            if self.conn.query(self.table).get(id=objeto.id):
                self.conn.merge(objeto)
                self.conn.commit()
                return objeto
            else:
                raise Exception("No existe")
        except Exception as e:
            raise Exception(str(e))

    def delete(self, identificador):
        try:
            self.conn.delete(identificador)
            self.conn.commit()
            return True
        except Exception as e:
            raise Exception(str(e))

    def findAll(self):
        try:
            objetos = self.conn.query(self.table).all()
            self.conn.commit()
            return objetos
        except Exception as e:
            raise Exception(str(e))
