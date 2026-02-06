from typing import Dict
from fastapi import HTTPException
from sqlalchemy.orm import Session
from src.models.entities.person import Person
from src.models.repository.person_repository import person_repository

class PeopleFinderController:
    def find_by_name(self, name: str, db: Session) -> Dict:
        try:
            self.__validate_name(name)

            person = person_repository.find_person_by_name(name=name, db=db)

            if not person:
                raise HTTPException(status_code=404, detail="Pessoa não encontrada")

            response = self.__format_response(person)

            return response
        except HTTPException:
            raise
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
        
    def find_all(self, db: Session) -> Dict:
        try:

            people = person_repository.find_all(db=db)

            response = self.__format_response(people)

            return response
        except HTTPException:
            raise
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
    

    def __validate_name(self, name: str) -> None:
        if not isinstance(name, str):
            raise HTTPException(status_code=400, detail="Campo nome está incorreto")

        if name.isnumeric():
            raise HTTPException(status_code=400, detail="Campo nome está incorreto")


    def __format_response(self, people: list[Person]) -> Dict:
        data = []

        for person in people:
            data.append({
                'name': person.name,
                'age': person.age,
                'height': person.height
            })

        return {
            'count': len(data),
            'type': 'Person',
            'infos': data
        }