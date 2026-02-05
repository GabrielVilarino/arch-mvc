from passlib.context import CryptContext
from src.models.entities.user import User
from typing import Optional
class UserRepository:

    def __init__(self):
        self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

        self.login = User(1, "admin", self.pwd_context.hash("123456"))

    def find_by_username(self, username: str) -> Optional[User]:
        if self.login.username == username:
            return self.login

        return None
    
    def verify_password(self, plain, hashed):
        return self.pwd_context.verify(plain, hashed)
    
user_repository = UserRepository()