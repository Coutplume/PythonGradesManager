from app import db


class Class(db.Model):
    __tablename__ = 'class'
    class_id = db.Column(db.Integer, primary_key=True)
    class_name = db.Column(db.String(80), unique=False)
    tutor_id = db.Column(db.Integer, unique=False)
    queue = db.Column(db.Integer, unique=False)
    grade = db.Column(db.String(80), unique=False)


def get_class_id(class_name: str, grade: str):
    res = db.session.query(Class).filter_by(class_name=class_name, grade=grade).first()
    if res is None:
        return -1
    else:
        return res.class_id


def get_class_name(class_id: int) -> str:
    res = db.session.query(Class).filter_by(class_id=class_id).first()
    if res is None:
        return 'none'
    else:
        return res.class_name


def get_all_class():
    return db.session.query(Class).all()


def has_class(class_name, grade) -> bool:
    res = db.session.query(Class).filter_by(class_name=class_name, grade=grade).first()
    if res is not None:
        return True
    else:
        return False


def change_class(class_id, class_name, grade, tutor_id, queue_id):
    res = db.session.query(Class).filter_by(class_id=class_id).first()
    res.class_name = class_name
    res.grade = grade
    res.tutor_id = tutor_id
    res.queue = queue_id
    db.session.add(res)
    db.session.commit()


def add_class(class_name, grade, tutor_id, queue_id):
    res = Class()
    res.class_name = class_name
    res.grade = grade
    res.tutor_id = tutor_id
    res.queue = queue_id
    db.session.add(res)
    db.session.commit()
