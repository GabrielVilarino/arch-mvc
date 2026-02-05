from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from src.controllers.login_controller import LoginController
from src.schemas.auth_schema import TokenResponse, RefreshRequest

router = APIRouter(prefix="/auth", tags=["Auth"])
controller = LoginController()

@router.post("/login", response_model=TokenResponse)
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    return controller.login(
        username=form_data.username,
        password=form_data.password
    )

@router.post("/refresh")
def refresh(data: RefreshRequest):
    return controller.refresh(data.refresh_token)