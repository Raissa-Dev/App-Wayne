from pydantic import BaseModel

class UserLogin(BaseModel):
    tipo: str
    senha: str