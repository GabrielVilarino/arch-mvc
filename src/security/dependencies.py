from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from src.security.jwt import decode_token
from jose import JWTError

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = decode_token(token)

        if payload.get("type") != "access":
            raise HTTPException(status_code=401, detail="Token inválido")

        return payload

    except JWTError:
        raise HTTPException(status_code=401, detail="Token inválido")