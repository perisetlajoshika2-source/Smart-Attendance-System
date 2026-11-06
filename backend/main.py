from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Student(BaseModel):
    name: str

@app.get("/")
def home():
    return {"message": "Smart Attendance System Backend Running"}

@app.post("/mark_attendance")
def mark_attendance(student: Student):
    return {
        "student": student.name,
        "status": "Present"
    }