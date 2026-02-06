from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.models.connections.session import get_db
from src.security.dependencies import get_current_user
from src.controllers.people_finder_controller import PeopleFinderController

router = APIRouter()
controller = PeopleFinderController()

@router.get("/finder/person")
def find_person(
        name: str,
        user=Depends(get_current_user),
        db: Session = Depends(get_db)
    ):
    return controller.find_by_name(name=name, db=db)

@router.get("/finder/people")
def find_people(
        user=Depends(get_current_user),
        db: Session = Depends(get_db)
    ):
    return controller.find_all(db=db)
