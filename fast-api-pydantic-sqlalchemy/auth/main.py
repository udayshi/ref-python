from jose import JWTError, jwt


from fastapi import Depends, HTTPException, status
from .schema import  TokenData,  UserInDB
from .utils import get_user, oauth2_scheme, SECRET_KEY, ALGORITHM

#uday-oauth2passwd

db = {
    "uday": {
        "username": "uday",
        "full_name": "Uday Shiwakoti",
        "email": "uday@uday.com.np",
        "hashed_password": "$2b$12$iF4ovH2HLZmlRUpnAO21WeFE22cJev5MQz/ScGtJ81EquHhxKv8M6",
        "disabled": False
    }
}


async def get_current_user(token: str = Depends(oauth2_scheme)):
    credential_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                         detail="Could not validate credentials", headers={"WWW-Authenticate": "Bearer"})
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credential_exception

        token_data = TokenData(username=username)
    except JWTError:
        raise credential_exception

    user = get_user(db, username=token_data.username)
    if user is None:
        raise credential_exception

    return user


async def get_current_active_user(current_user: UserInDB = Depends(get_current_user)):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")

    return current_user
