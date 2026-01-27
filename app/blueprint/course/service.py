from .models import read_course_db, read_enrollment_db
from .models import create_course_db
import datetime
from flask import g


def read_course(id: int):
    data = read_course_db(id)
    if not data:
        raise ValueError("Course not found")
    return data


def create_course(dataCourse: dict):
    dataUser = g.dataUser
    if dataUser['role'] == 'student':
        raise ValueError("Only teachers can create courses")
    return create_course_db(dataCourse['title'], dataUser['user_id'], dataCourse['description'], datetime.datetime.now(datetime.timezone.utc))


def courses_taken():
    dataUser = g.dataUser
    result = read_enrollment_db(dataUser['user_id'])
    return result
