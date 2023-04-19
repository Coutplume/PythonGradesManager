from app import db


class Queue(db.Model):
    __tablename__ = 'queue'
    queue_id = db.Column(db.Integer, primary_key=True)
    queue_name = db.Column(db.String(80), unique=False)
    queue_grade = db.Column(db.String(80), unique=False)
    queue_cadre = db.Column(db.String(80), unique=False)


def get_queue_id(queue_name: str, queue_grade: str) -> int:
    res = db.session.query(Queue).filter_by(queue_name=queue_name, queue_grade=queue_grade).first()
    if res is None:
        return -1
    else:
        return res.queue_id


def get_queue_name(queue_id: int) -> str:
    res = db.session.query(Queue).filter_by(queue_id=queue_id).first()
    if res is None:
        return 'none'
    else:
        return res.queue_name


def get_all_queue():
    res = db.session.query(Queue).all()
    return res


def has_queue(queue_name, queue_grade):
    res = db.session.query(Queue).filter_by(queue_name=queue_name, queue_grade=queue_grade).first()
    if res is not None:
        return True
    else:
        return False


def add_queue(queue_name, queue_grade, queue_cadre):
    queue = Queue()
    queue.queue_grade = queue_grade
    queue.queue_cadre = queue_cadre
    queue.queue_name = queue_name
    db.session.add(queue)
    db.session.commit()


def change_queue(queue_id, queue_name, queue_grade, queue_cadre):
    queue = db.session.query(Queue).filter_by(queue_id=queue_id).first()
    queue.queue_grade = queue_grade
    queue.queue_cadre = queue_cadre
    queue.queue_name = queue_name
    db.session.add(queue)
    db.session.commit()
