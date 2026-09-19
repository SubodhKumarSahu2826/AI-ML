from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):

    name: str='Subodh Kumar Sahu'

    age: Optional[int]=None

    email:EmailStr
    cgpa: float=Field(gt=0, lt=10.0, description='A decimal value between 0 and 10 representing the cumulative grade point average of the student')

new_student={'age':21, 'email':'subodh@example.com', 'name':'Subodh Kumar Sahu', 'cgpa':5.0}

student=Student(**new_student)

student_dict=dict(student)

print(student_dict['age'])

student_json=student.model_dump_json()


