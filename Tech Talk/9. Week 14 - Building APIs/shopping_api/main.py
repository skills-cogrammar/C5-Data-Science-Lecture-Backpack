# Import system dependencies
import os 
from dotenv import load_dotenv

# Import FastAPI dependencies
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from fastapi import APIRouter

# Import routers 
from src.routers import product_router , user_auth_router , user_router

# Load the environment variables
load_dotenv()

app = FastAPI()

# Configure middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)


# Configure routers 
app.include_router(product_router.router)
app.include_router(user_auth_router.router)
app.include_router(user_router.router)

if __name__ == "__main__":
    uvicorn.run('main:app', host=os.getenv("HOST"), port=int(os.getenv("PORT")), 
                reload=os.getenv("REOLOAD"))