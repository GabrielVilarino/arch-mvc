from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.models.connections.session import get_db
from fastapi.security import OAuth2PasswordRequestForm
from src.controllers.login_controller import LoginController
from src.schemas.auth_schema import TokenResponse, RefreshRequest

router = APIRouter(prefix="/auth", tags=["Auth"])
controller = LoginController()

@router.post("/login", response_model=TokenResponse)
def login(
        form_data: OAuth2PasswordRequestForm = Depends(),
        db: Session = Depends(get_db)
    ):
    return controller.login(
        username=form_data.username,
        password=form_data.password,
        db=db
    )

@router.post("/refresh")
def refresh(data: RefreshRequest):
    return controller.refresh(data.refresh_token)