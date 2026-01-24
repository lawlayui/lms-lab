from flask import g 
from app.utils.db import get_db

def read_user(user_id: int=None, username: str = None, role: str = None):
    db = get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute('select * from users where id = %s or username = %s',(user_id, username))
    data = cursor.fetchone()
    cursor.close()
    return data

def create_user(username: str, password: str, role: str):
    db = get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute('insert into users(username, password, role) values(%s, %s, %s)',(username, password, role))
    user_id = cursor.lastrowid
    db.commit()
    cursor.close()
    return user_id
