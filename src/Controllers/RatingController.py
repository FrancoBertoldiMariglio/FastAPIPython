from fastapi import APIRouter
from .BaseControllerImp import BaseControllerImplement as service

routerRaiting = APIRouter()


class RatingControllerImplement(service):
    dir = 'rating'
