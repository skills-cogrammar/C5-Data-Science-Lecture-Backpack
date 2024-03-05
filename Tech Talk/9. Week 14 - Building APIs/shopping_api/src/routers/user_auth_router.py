from fastapi import APIRouter, Depends, HTTPException, status

from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from jose import jwt, JWTError

from src.controllers.user_auth_controller import UserAuthController
from src.models.user_auth_request_model import UserAuthRequest

import os 
from dotenv import load_dotenv

load_dotenv()

router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)

contoller = UserAuthController('sqlite:///resources/store.db')


async def validate_user_token(token: str = Depends(OAuth2PasswordBearer(tokenUrl="auth/login"))):
    try:
        payload = jwt.decode(token, os.getenv("SECRET_KEY"), algorithms=['HS256'])
        user_id = payload.get("id")
        
        if not user_id:
            return False
        
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")
    
    return user_id


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_user(user: UserAuthRequest):
    contoller.create_user(user)
    return {
        "message": "User created successfully"
    }
    

@router.get("/token")
async def generate_api_token():    
    return contoller.generate_api_token()    
    

@router.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = contoller.authenticate_user(form_data.username, form_data.password)

    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid username or password")
    
    token = contoller.create_access_token(user['user_id'])

    return {
        "access_token": token,
        "token_type": "bearer"
    }

@router.get("/user")
async def get_user(user: str = Depends(validate_user_token)):
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid username or password")
    return {
        "User": user
    }
