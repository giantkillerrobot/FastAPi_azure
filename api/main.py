from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi import Response
import pymssql
import json

app = FastAPI()

fakedb = []

class Course(BaseModel):
    id:int
    name:str
    price:float
    is_early_bird: Optional[bool] = None
 

@app.get("/")
def get_home():
    return {"message": "Hello World - Ankit Rocks!  Testing From VS"}

@app.get("/db")
def db_test():
    conn = pymssql.connect(
    server="40.114.74.64",
    port=1401,
    user="amvmdev23",
    password="AMvmdev-2023!",
    database="AM_PRIME_2_DEV")
  
    print("conn done")
    cursor = conn.cursor(as_dict=True)
    print("cursor done")
    cursor.execute('SELECT name_last, name_first, current_latest_position FROM people')
    json_string = json.dumps(cursor.fetchall()) 
    #row = cursor.fetchone()
    #for row in cursor:
    #    the_row_id = row['id']
    #    print(row['id'])
        
    conn.close()

    return json_string

    return the_row_id


@app.get("/courses")
def get_courses():
    return fakedb


@app.get("/courses/{course_id}")
def get_course(course_id:int):
    course = course_id - 1
    return fakedb[course]


@app.post("/courses")
def add_course(course: Course):
    fakedb.append(course.dict())
    return fakedb[-1]

@app.delete("/courses")
def delete_course(course_id: int):
    fakedb.pop(course_id - 1)
    return {"message": "deleted successfully"}    
