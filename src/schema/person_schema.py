from pydantic import BaseModel

class PersonRegisterRequest(BaseModel):
    name: str
    age: int
    height: float

class PersonResponse(BaseModel):
    name: str
    age: int
    height: float