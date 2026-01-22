from flask import g 
from app.utils.db import get_db
from app.utils.security import generate_hash

def read_user(user_id: int, username: str):
    db = get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute('select * from users where id = %s, username = %s',(user_id, username.strip()))
    data = cursor.fetchone
    return data

def create_user(username, password):
    db = get_db()
    cursor = db.cursor(dictionary=True)
    username = username.strip()
    password = generate_hash(password.strip())
    cursor.execute('insert into users(username, password) values(%s, %s)',(username, password))
    return 
