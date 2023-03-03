from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi import Response
import pymssql
import json
import requests


app = FastAPI()

fakedb = []

class Course(BaseModel):
    id:int
    name:str
    price:float
    is_early_bird: Optional[bool] = None
 

@app.get("/")
def get_home():
    ip = requests.get('https://api.ipify.org').text
    return {"message": f" my ip is {ip}"}

@app.get("/db")
def db_test():
    try:
        conn = pymssql.connect(
        server="40.114.74.64",
        port=1401,
        user="amvmdev23",
        password="AMvmdev-2023!",
        database="AM_PRIME_2_DEV")
        
        
    except Exception as e:
        print("e==",e)
        return str(e)
    
    cursor = conn.cursor(as_dict=True)
    cursor.execute('SELECT name_last, name_first, current_latest_position FROM people')
    json_string = json.dumps(cursor.fetchall()) 
    conn.close()
    return json_string


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
