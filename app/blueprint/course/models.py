from app.utils.db import get_db


def read_course_db(id: int):
    db = get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute('select * from course where id = %s', (id,))
    data = cursor.fetchone()
    cursor.close()
    return data


def read_enrollment_db(id: int):
    db = get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute('select * from enrollment where student_id = %s', (id,))
    data = cursor.fetchall()
    cursor.close()
    return data


def create_course_db(title: str, teacher_id: int, description: str, release_date: str):
    db = get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute('insert into course (title, teacher_id, description, release_date) values (%s, %s, %s, %s)',
                   (title, teacher_id, description, release_date))
    course_id = cursor.lastrowid
    db.commit()
    cursor.close()
    return course_id


def delete_course_db(id: int):
    db = get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute('delete from course where id = %s', (id,))
    db.commit()
    cursor.close()


def leave_course_db(id: int):
    db = get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute('delete form enrollment where course_id = %s', (id,))
    db.commit()
    cursor.close()
