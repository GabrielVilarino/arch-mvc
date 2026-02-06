from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.models.connections.session import get_db
from src.security.dependencies import get_current_user
from src.controllers.people_register_controller import PeopleRegisterController
from src.schemas.person_schema import PersonRegisterRequest

from typing import Dict

router = APIRouter()
controller = PeopleRegisterController()

@router.post("/register/person")
def register_person(
        new_person_information: PersonRegisterRequest,
        user=Depends(get_current_user),
        db: Session = Depends(get_db)
    ):
    return controller.register(
        new_person_information=new_person_information,
        db=db
    )
