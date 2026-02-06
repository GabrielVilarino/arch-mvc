from sqlalchemy.orm import Session
from passlib.context import CryptContext
from src.models.entities.user import User
from typing import Optional

class UserRepository:

    def __init__(self):
        self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def find_by_username(self, username: str, db: Session) -> Optional[User]:
        return db.query(User).filter(User.username == username).first()
    
    def verify_password(self, plain, hashed):
        return self.pwd_context.verify(plain, hashed)
    
user_repository = UserRepository()