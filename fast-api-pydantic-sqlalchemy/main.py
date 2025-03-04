from fastapi import FastAPI, Depends,  Request

from item.router import rtr as item_router
from auth.router import rtr as auth_router
from auth.main import get_current_active_user


#from auth.utils import 
app = FastAPI()

app.include_router(item_router)
app.include_router(auth_router)

# @app.middleware("http")
# async def oauth2_middleware(request: Request, call_next):
#     # Extract and validate the token from the Authorization header
#     token = request.headers.get("Authorization")
#     #logics to validate the token
#     print("Trapped in middleware",token)
#     response = await call_next(request)
#     return response