from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from src.models.product import Product
from src.controllers.product_controller import ProductController
from src.controllers.user_auth_controller import UserAuthController

import os 
from dotenv import load_dotenv

load_dotenv()

router = APIRouter(
    prefix="/product",
    tags=["Product"]
)

controller = ProductController('sqlite:///resources/store.db')
auth_controller = UserAuthController('sqlite:///resources/store.db')

async def validate_user_token(token: str = Depends(OAuth2PasswordBearer(tokenUrl="auth/login"))):
    try:
        payload = jwt.decode(token, os.getenv("SECRET_KEY"), algorithms=['HS256'])
        user_id = payload.get("id")
        
        if not user_id:
            return False
        
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")
    
    return user_id

@router.get("/", status_code=200)
async def get_all(api_token: str):
    if not auth_controller.is_valid_token(api_token):
        raise HTTPException(status_code=401, detail="Unauthorized")
        
    result = controller.get_all()
    return {
        "products": result
    }
    
@router.get("/{id}")
async def get(id: str, api_token: str):
    if not auth_controller.is_valid_token(api_token):
        raise HTTPException(status_code=401, detail="Unauthorized")

    result = controller.get(id)
    return {
        'product': result
    }
    
@router.post("/", status_code=200)
async def create(product: Product, user: str = Depends(validate_user_token)):
    if not user:
        raise HTTPException(status_code=401, detail="Unauthorized")
    
    if not controller.is_admin(user):
        raise HTTPException(status_code=401, detail="Unauthorized")

    controller.create(product)
    return {
        "message": "Created"
    }

@router.put("/", status_code=200)
async def update(product: Product, user: str = Depends(validate_user_token)):
    if not user:
        raise HTTPException(status_code=401, detail="Unauthorized")
    
    if not controller.is_admin(user):
        raise HTTPException(status_code=401, detail="Unauthorized")
    
    controller.update(product)

    return {
        "message": "updated"
        }