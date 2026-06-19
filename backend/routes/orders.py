from fastapi import APIRouter

from backend.models.order import Order


routes = APIRouter(
    prefix = '/orders',
    tags = ['orders']
)

@routes.post('/orders')
def orders():
    ...