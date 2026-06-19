from fastapi import APIRouter

from backend.database import get_db
from backend.models.user import User


router = APIRouter(
    prefix ='/auth',
    tags = ['authentication']
)

@router.get('/test')
def test_auth ():               # Temporary | only used to test if it works
    return{
    'message':'auth works!!'
    }

@router.post('/signup')
def signup():
    ...

@router.post('/login')
def login():
    ...