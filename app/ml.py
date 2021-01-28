"""Machine learning functions"""

from fastapi import APIRouter

router = APIRouter()

@router.get('/hello_user_ml')
async def hello_user(name = 'Ike'):
    '''Return simple gretting'''
    return {'username' : f'Hello {name}'}