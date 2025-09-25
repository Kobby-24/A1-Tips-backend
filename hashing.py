from passlib.context import CryptContext


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Hashing utility class for password hashing
class Hash():
    def bcrypt(self, password: str) -> str:
        return pwd_context.hash(password)
    def verify(self, hashed_password: str, plain_password: str) -> bool:
        return pwd_context.verify(plain_password, hashed_password)