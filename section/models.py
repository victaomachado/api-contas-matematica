from typing import Optional

from pydantic import BaseModel, validator

class Curso(BaseModel):
    id: Optional[int] = None
    titulo: str
    aulas: int
    horas: int

cursos = [
    Curso(id=1, titulo="Meu primeiro codigo", aulas=45, horas=94),
    Curso(id=2, titulo="Java POO", aulas=32, horas=93)
]