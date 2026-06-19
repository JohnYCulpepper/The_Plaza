from fastapi import APIRouter

router = APIRouter(
    prefix ='/auth',
    tags = {'authentication'}
)


@router.get('/test')

# Temporary | only used to test if it works
def test_auth ():
    return{
    'message':'auth works!!'
    }
