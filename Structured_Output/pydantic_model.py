from pydantic import BaseModel


class Student(BaseModel):
    student_name:str
    
new_std={"student_name":"Nirmal"}

res=Student(**new_std)
print(res)