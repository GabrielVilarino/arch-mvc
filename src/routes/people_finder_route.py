from fastapi import APIRouter, HTTPException
from src.controllers.people_finder_controller import PeopleFinderController

router = APIRouter()
controller = PeopleFinderController()

@router.get("/finder/people")
def find_person(name: str):

    response = controller.find_by_name(name)

    if not response['success']:
        raise HTTPException(status_code=400, detail=response['error'])
    
    return response['message']

@router.get("/finder/all-people")
def find_all_people():
    response = controller.find_all()

    if not response['success']:
        raise HTTPException(status_code=400, detail=response['error'])
    
    return response['message']
