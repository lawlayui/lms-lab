from app.utils.db import get_db


def create_enrollment_db(student_id: int, course_id: int, date_entry: int):
    db = get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute('insert into enrollment(student_id, course_id, date_entry) values(%s, %s, %s)',
                   (student_id, course_id, date_entry))
    db.commit()
    cursor.close()
