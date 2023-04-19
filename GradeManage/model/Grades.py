from app import db


class Grades(db.Model):
    __tablename__ = 'grades'
    grades_id = db.Column(db.Integer, primary_key=True)
    sid = db.Column(db.Integer, unique=False)
    time = db.Column(db.String(80), unique=False)
    grades = db.Column(db.String(80), unique=False)
    grades_type = db.Column(db.String(80), unique=False)


def add_grade(sid, time, grades, grades_type) -> int:
    # 检测是否有重复成绩
    res = db.session.query(Grades).filter_by(sid=sid, time=time, grades_type=grades_type).first()
    if res is not None:
        return -1
    data = Grades()

    data.sid = sid
    data.grades_type = grades_type
    data.grades = grades
    data.time = time

    db.session.add(data)
    db.session.commit()
    return 0


def get_all_grades():
    return db.session.query(Grades).all()


def get_all_grades_by_id(sid: int):
    return db.session.query(Grades).filter_by(sid=sid).all()


