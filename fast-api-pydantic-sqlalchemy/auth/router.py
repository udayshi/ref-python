from fastapi import APIRouter,Depends, HTTPException,status
from fastapi.security import  OAuth2PasswordRequestForm

from .utils import create_access_token,authenticate_user, ACCESS_TOKEN_EXPIRE_MINUTES
from .schema import Token
from .main import db

from datetime import  timedelta
rtr=APIRouter()


@rtr.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Incorrect username or password", headers={"WWW-Authenticate": "Bearer"})
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires)
    return {"access_token": access_token, "token_type": "bearer"}