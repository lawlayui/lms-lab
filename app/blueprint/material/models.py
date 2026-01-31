from app.utils.db import get_db


def read_materail_db(id: int):
    db = get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute('select * from material where course_id = %s', (id,))
    data = cursor.fetchall()
    cursor.close()
    return data


def create_material_db(title: str, description: str, course_id: int):
    db = get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute('insert into material(title, description, course_id) values(%s, %s, %s)',
                   (title, description, course_id))
    db.commit()
    cursor.close()
