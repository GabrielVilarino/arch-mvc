from typing import Dict
from fastapi import HTTPException
from src.models.entities.person import Person
from src.schemas.person_schema import PersonRegisterRequest
from src.models.repository.person_repository import person_repository

class PeopleRegisterController:
    def register(self, new_person_information: PersonRegisterRequest) -> Dict:
        try:
            self.__validate_fields(new_person_information)         
            new_person_information = self.__format_fields(new_person_information)

            self.__verify_person(new_person_information)
            self.__register_person(new_person_information)

            response = self.__format_response(new_person_information)

            return response
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))


    def __validate_fields(self, new_person_information: PersonRegisterRequest) -> None:
        if not isinstance(new_person_information.name, str):
            raise ValueError("Campo nome está incorreto")
        
        try:
            int(new_person_information.age)
        except Exception:
            raise ValueError("Campo idade está incorreto")
        
        try:
            float(new_person_information.height)
        except Exception:
            raise ValueError("Campo altura está incorreto")


    def __format_fields(self, new_person_information: PersonRegisterRequest) -> PersonRegisterRequest:
    
        if new_person_information.height > 100:
            new_person_information.height = round(new_person_information.height / 100, 2)
        
        return new_person_information


    def __verify_person(self, new_person_information: PersonRegisterRequest) -> None:
        person = person_repository.find_person_by_name(new_person_information.name)

        if person:
            raise Exception('Pessoa ja cadastrada')


    def __register_person(self, new_person_information: PersonRegisterRequest) -> None:
        try:
            person = Person(new_person_information.name, new_person_information.age, new_person_information.height)
        except Exception:
            raise Exception('Erro ao instanciar pessoa')

        try:
            repository = person_repository
            repository.registry_person(person)
        except Exception:
            raise Exception('Erro ao cadastrar pessoa')
        
    def __format_response(self, new_person_information: PersonRegisterRequest) -> Dict:
        return {
            'count': 1,
            'type': 'Person',
            'attributes': new_person_information
        }
