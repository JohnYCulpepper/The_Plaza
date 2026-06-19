from fastapi import APIRouter

from backend.models.product import Product


routes = APIRouter(
    prefix = '/products',
    tags = ['products']
)

@routes.post('/products')
def products():
    ...