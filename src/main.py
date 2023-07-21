from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from utils.settings import settings
from utils.response import ServerError, Error
from database.model import Skill, Student
# ASYNC engine
from database.client import async_engine


app = FastAPI()

# CORS settings
app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.cors_allow_origin],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Exception handle
@app.exception_handler(Exception)
async def validation_exception_handler(request, e):
    return ServerError(e)

@app.exception_handler(ValueError)
async def validation_exception_handler(request, e):
    return Error(e)

# API with ASYNC Mongo engine

@app.get("/")
async def root():
    return {
        "app_name": settings.app_name,
        "environement": settings.environment,
        "status": 'RUNNING'
    }

@app.post("/skill", response_model=Skill) # On POST 'response_model' is important to display whole Model data
async def create_skill(skill: Skill):
    await async_engine.save(skill)
    return skill

@app.post("/student", response_model=Student) # On POST 'response_model' is important to display whole Model data
async def create_student(student: Student):
    await async_engine.save(student)
    return student

@app.get("/skills")
async def students():
    students = await async_engine.find(Student)
    return students

@app.get("/students")
async def students():
    students = await async_engine.find(Student)
    return students