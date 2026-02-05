from typing import Dict
from src.models.entities.person import Person
from src.models.repository.person_repository import person_repository

class PeopleFinderController:
    def find_by_name(self, name: str) -> Dict:
        try:
            
            if not isinstance(name, str):
                raise ValueError("Campo nome está incorreto")
    
            if name.isnumeric():
                raise ValueError("Campo nome está incorreto")

            person = person_repository.find_person_by_name(name)

            if not person:
                raise Exception('Pessoa não encontrada')

            response = self.__format_response(person)

            return {
                'success': True,
                'message': response
            }
        except Exception as e:
            return {
                'success': False,
                'error': str(e)
            }
        
    def find_all(self) -> Dict:
        try:

            people = person_repository.find_all()

            response = self.__format_response(people)

            return {
                'success': True,
                'message': response
            }
        except Exception as e:
            return {
                'success': False,
                'error': str(e)
            }
    

    def __validate_fields(self, person_finder_information: Dict) -> None:
        name = person_finder_information.get("name")

        if not isinstance(name, str):
            raise ValueError("Campo nome está incorreto")
 
        if name.isnumeric():
            raise ValueError("Campo nome está incorreto")


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