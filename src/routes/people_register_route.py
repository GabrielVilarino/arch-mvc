from fastapi import APIRouter, HTTPException
from src.controllers.people_register_controller import PeopleRegisterController
from src.schema.person_schema import PersonRegisterRequest

from typing import Dict

router = APIRouter()
controller = PeopleRegisterController()

@router.post("/register/person")
def register_person(new_person_information: PersonRegisterRequest):

    response = controller.register(new_person_information)

    if not response['success']:
        raise HTTPException(status_code=400, detail=response['error'])
    
    return response['message']