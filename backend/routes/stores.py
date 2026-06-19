from fastapi import APIRouter

from backend.models.store import Store


routes = APIRouter(
    prefix = '/store',
    tags = ['store']
)

@routes.post('/stores')
def stores():
    ...