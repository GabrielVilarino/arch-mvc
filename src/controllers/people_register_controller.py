from typing import Dict
from fastapi import HTTPException
from sqlalchemy.orm import Session
from fastapi import HTTPException
from src.models.entities.person import Person
from src.schemas.person_schema import PersonRegisterRequest
from src.models.repository.person_repository import person_repository

class PeopleRegisterController:
    def register(self, new_person_information: PersonRegisterRequest, db: Session) -> Dict:
        try:
            self.__validate_fields(new_person_information)         
            new_person_information = self.__format_fields(new_person_information)

            self.__verify_person(new_person_information=new_person_information, db=db)
            self.__register_person(new_person_information=new_person_information, db=db)

            response = self.__format_response(new_person_information)

            return response
        except HTTPException:
            raise
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))


    def __validate_fields(self, new_person_information: PersonRegisterRequest) -> None:
        if not isinstance(new_person_information.name, str):
            raise HTTPException(status_code=400, detail="Campo nome está incorreto")
        
        try:
            int(new_person_information.age)
        except Exception:
            raise HTTPException(status_code=400, detail="Campo idade está incorreto")
        
        try:
            float(new_person_information.height)
        except Exception:
            raise HTTPException(status_code=400, detail="Campo altura está incorreto")


    def __format_fields(self, new_person_information: PersonRegisterRequest) -> PersonRegisterRequest:
    
        if new_person_information.height > 100:
            new_person_information.height = round(new_person_information.height / 100, 2)
        
        return new_person_information


    def __verify_person(self, new_person_information: PersonRegisterRequest, db: Session) -> None:
        person = person_repository.find_person_by_name(
            name=new_person_information.name,
            db=db
        )

        if person:
            raise HTTPException(status_code=400, detail='Pessoa ja cadastrada')


    def __register_person(self, new_person_information: PersonRegisterRequest, db: Session) -> None:
        try:
            person = Person(
                name=new_person_information.name,
                age=new_person_information.age,
                height=new_person_information.height
            )
        except Exception as e:
            raise Exception(f'Erro ao instanciar pessoa: {str(e)}')

        try:
            repository = person_repository
            repository.registry_person(person=person, db=db)
        except Exception as e:
            raise Exception(f'Erro ao cadastrar pessoa: {str(e)}')
        
    def __format_response(self, new_person_information: PersonRegisterRequest) -> Dict:
        return {
            'count': 1,
            'type': 'Person',
            'attributes': new_person_information
        }
