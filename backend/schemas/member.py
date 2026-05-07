from pydantic import BaseModel

class Member(BaseModel):
    id: int
    nombre: str
    curso: str
    rol: str | int

class MemberIn(BaseModel):
    nombre: str
    curso: str
    rol: str