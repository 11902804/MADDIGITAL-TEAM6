from fastapi import APIRouter, HTTPException, Response, Depends
from app.infrastructure.mock.auth_repository import AuthRepository, AuthenticationError
from fastapi_jwt_auth import AuthJWT
from fastapi_jwt_auth.exceptions import AuthJWTException
from pydantic import BaseModel
import time

router = APIRouter()

# Mariel note: shouldn't this classes, User and Settings be defined appart? In model?
class User(BaseModel):
    email: str
    password: str

class Settings(BaseModel):
    authjwt_secret_key: str = "0yyDy8Z5HYEowef6uvxP"

@AuthJWT.load_config
def get_config():
    return Settings()

@router.post('/auth/login')
def login_user(user: User, Authorize: AuthJWT = Depends()):

    try:
        # Selecting user from database
        status, name = AuthRepository().login(user.email, user.password)
    except AuthenticationError as error:
        print(error)
        return {'error': str(error)}
    except Exception as error:
        return {'error': 'An unknown error has occurred!'}

    access_token = Authorize.create_access_token(subject=user.email)
    return {"access_token": access_token, "name": name}
    