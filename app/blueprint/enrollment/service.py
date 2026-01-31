from .models import create_enrollment_db
from flask import g 
import datetime 


def create_enrollment(course_id: int):
    dataUser = g.dataUser 

    if dataUser['role'] == 'teacher':
        raise ValueError("teacher role cannot follow the course")
    
    create_enrollment_db(dataUser['user_id'], course_id, datetime.datetime.now(datetime.timezone.utc))