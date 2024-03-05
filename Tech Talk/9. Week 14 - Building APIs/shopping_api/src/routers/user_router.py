from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from src.models.user import User
from src.controllers.user_controller import UserController 

import os 
from dotenv import load_dotenv

load_dotenv()

router = APIRouter(
    prefix="/user",
    tags=["user"]
)

controller = UserController('sqlite:///resources/store.db')


async def validate_user_token(token: str = Depends(OAuth2PasswordBearer(tokenUrl="auth/login"))):
    try:
        payload = jwt.decode(token, os.getenv("SECRET_KEY"), algorithms=['HS256'])
        user_id = payload.get("id")
        
        if not user_id:
            return False
        
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")
    
    return user_id


@router.put("/")
def update_user(user_details: User, user: str = Depends(validate_user_token)):
    if not user:
        raise HTTPException(status_code=401, detail="Unauthorized")
    
    if not controller.is_admin(user):
        raise HTTPException(status_code=401, detail="Unauthorized")
    

    controller.update(user_details)
    return {
        "message": "updated"
    }       
    

@router.get("/")
async def get_user(user: str = Depends(validate_user_token)):
    if not user:
        raise HTTPException(status_code=401, detail="Unauthorized")
    
    result = controller.get_user(user)        
    
    if result is None:
        raise HTTPException(status_code=404, detail="User not found")
    
    return {
        "user": result
    }
    
@router.post("/cart")
def add_to_cart(product_id: str, user: str = Depends(validate_user_token)):
    if not user:
        raise HTTPException(status_code=401, detail="Unauthorized")
        
    controller.add_to_cart(user, product_id)
    return {
        "message": "added to cart"
    }
    
@router.post("/{id}/wishlist")
def add_to_wishlist(id: str, product_id: str, user: str = Depends(validate_user_token)):
    if not user:
        raise HTTPException(status_code=401, detail="Unauthorized")

    controller.add_to_wishlist(id, product_id)
    return {
        "message": "added to wishlist"
    }