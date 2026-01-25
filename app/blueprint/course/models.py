from app.utils.db import get_db

def read_course(id:int):
    db = get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute('select * from course where id = %s',(id,))
    data = cursor.fetchone()
    cursor.close()
    return data