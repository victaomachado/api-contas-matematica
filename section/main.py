from fastapi import FastAPI

from models import Curso
from models import cursos

app = FastAPI(title="Unisagrado API")

@app.get("/sum/{num1}/{num2}")
async def sum(num1: int, num2: int):
    sum_result = num1 + num2
    return {"Sum": sum_result}

@app.get("/subtr/{num1}/{num2}")
async def subtr(num1: int, num2: int):
    subtr_result = num1 - num2
    return {"Subtr": subtr_result}

@app.get("/mult/{num1}/{num2}")
async def mult(num1: int, num2: int):
    mult_result = num1 * num2
    return {"Mult": mult_result}

@app.get("/div/{num1}/{num2}")
async def div(num1: int, num2: int):
    div_result = num1 / num2
    return {"Div": div_result}

@app.get("/cursos")
async def get_cursos():
    return cursos


@app.post("/curso")
async def post_method(curso: Curso):
    next_id: int = len(cursos) + 1
    curso.id = next_id
    cursos.append(curso)
    return curso


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)