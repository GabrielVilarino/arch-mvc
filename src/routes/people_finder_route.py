from fastapi import APIRouter, Depends
from src.security.dependencies import get_current_user
from src.controllers.people_finder_controller import PeopleFinderController

router = APIRouter()
controller = PeopleFinderController()

@router.get("/finder/people")
def find_person(name: str, user=Depends(get_current_user)):
    return controller.find_by_name(name)

@router.get("/finder/all-people")
def find_all_people(user=Depends(get_current_user)):
    return controller.find_all()
