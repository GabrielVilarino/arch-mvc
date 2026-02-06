from fastapi import HTTPException
from sqlalchemy.orm import Session
from src.models.entities.person import Person

class PersonRepository:

    def registry_person(self, person: Person, db: Session) -> None:
        try:
            db.add(person)
            db.commit()
            db.refresh(person)
        except Exception as e:
            raise Exception(str(e))


    def find_person_by_name(self, name: str, db: Session) -> list[Person]:
        return db.query(Person).filter(Person.name == name).all()


    def find_all(self, db: Session) -> list[Person]:
        people = db.query(Person).all()

        if not people:
            raise HTTPException(status_code=404, detail="Nenhuma pessoa cadastrada")

        return people


person_repository = PersonRepository()
