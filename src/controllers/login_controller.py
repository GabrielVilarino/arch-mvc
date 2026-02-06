from fastapi import HTTPException
from sqlalchemy.orm import Session
from fastapi import HTTPException
from src.models.repository.user_repository import user_repository
from src.security.jwt import (
    create_access_token,
    create_refresh_token,
    decode_token
)
from jose import JWTError

class LoginController:

    def login(self, username: str, password: str, db: Session) -> dict:
        try:
            user = user_repository.find_by_username(username=username, db=db)

            if not user or not user_repository.verify_password(password, user.password):
                raise HTTPException(
                    status_code=401,
                    detail="Usuário ou senha inválidos"
                )
            
            payload = {"sub": user.username, "user_id": user.id}

            return {
                "access_token": create_access_token(payload),
                "refresh_token": create_refresh_token(payload)
            }
        except HTTPException:
            raise
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))


    def refresh(self, refresh_token: str):
        try:
            payload = decode_token(refresh_token)

            if payload.get("type") != "refresh":
                raise HTTPException(status_code=401, detail="Token inválido")

            data = {
                "sub": payload["sub"],
                "user_id": payload["user_id"]
            }

            return {
                "access_token": create_access_token(data)
            }

        except JWTError:
            raise HTTPException(status_code=401, detail="Refresh token inválido")