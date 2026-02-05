from src.models.entities.person import Person

class PersonRepository:
    def __init__(self) -> None:
        self.__people: list[Person] = []

    def registry_person(self, person: Person) -> None:
        try:
            self.__people.append(person)
        except Exception:
            raise Exception("Erro ao cadastrar pessoa")

    def find_person_by_name(self, name: str) -> Person:
        for person in self.__people:
            if person.name == name:
                return [person]
        return None
    
    def find_all(self) -> list[Person]:

        if len(self.__people) == 0:
            raise Exception("Nenhuma pessoa cadastrada")

        return self.__people
    
person_repository = PersonRepository()