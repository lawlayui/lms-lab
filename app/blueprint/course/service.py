from .models import read_course

def get_information_course(id:int):
    data = read_course(id)
    if not data:
        raise ValueError("Course not found")
    return data