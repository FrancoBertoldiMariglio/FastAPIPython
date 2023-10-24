from fastapi import FastAPI, APIRouter, Depends
from src.Controllers.ProductoController import routerProdcto
from src.Controllers.RatingController import routerRaiting
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
import uvicorn


def main():
    app = FastAPI()

    app.include_router(routerProdcto, prefix="/producto", tags=["productos"])
    app.include_router(routerRaiting, prefix="/rating", tags=["ratings"])

    DATABASE_URL = "sqlite:///./test.db"

    if not os.path.exists("./test.db"):
        engine = create_engine(DATABASE_URL)
        SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
        Base = declarative_base()
        Base.metadata.create_all(bind=engine)
        db = SessionLocal()
        try:
            yield db
        finally:
            db.close()

    uvicorn.run(app, host="127.0.0.1", port=8000)


# uvicorn main:app --reload


if __name__ == "__main__":
    main()
