from pydantic import BaseModel, EmailStr, Field
from typing import Optional


class Student(BaseModel):
    
    name: str
    age: Optional[int] = None
    email: EmailStr
    cgpa: float = Field(gt=0, lt=9, default=5, description = 'A decimal value containing the cgpa')
    
new_student = {'name': 'muneeb', 'email': 'abc@gmail.com', 'cgpa':'8'}

student = Student(**new_student)

student_dict = dict(student)
student_json = student.model_dump_json()

print(student.email)