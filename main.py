from fastapi import FastAPI
from models import Student
from database import collection

app = FastAPI()

@app.post("/students")
async def create_student(student: Student):
    student_dict = student.dict()
    await collection.insert_one(student_dict)
    return {"message": "Student stored successfully"}

@app.get("/students")
async def get_students():
    students = []
    async for student in collection.find():
        student["_id"] = str(student["_id"])
        students.append(student)
    return students
