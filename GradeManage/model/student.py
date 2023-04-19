from app import db
from model import queue, Class


class Student(db.Model):
    __tablename__ = 'student'
    sid = db.Column(db.Integer, primary_key=True)
    sno = db.Column(db.String(80), unique=True)
    sname = db.Column(db.String(80), unique=False)
    class_id = db.Column(db.Integer, unique=False)
    queue_id = db.Column(db.Integer, unique=False)
    grade = db.Column(db.String(80), unique=False)
    password = db.Column(db.String(80), unique=False)

    def __str__(self):
        return '学号：{}, 名字：{}'.format(self.sno, self.sname)


def add_student(sno: str, sname: str, class_name: str, grade: str, queue_name: str) -> int:
    student = Student()
    query = db.session.query(Student).filter_by(sno=sno).first()
    if query is not None:
        print('学号已存在！')
        return -1
    student.sno = sno
    student.sname = sname
    student.grade = grade
    student.password = '123456'

    queue_id = queue.get_queue_id(queue_name=queue_name, queue_grade=grade)
    if queue_id == -1:
        print('连队不存在！')
        return -1
    student.queue_id = queue_id
    class_id = Class.get_class_id(class_name=class_name, grade=grade)
    if class_id == -1:
        print('教学班不存在！')
        return -1
    student.class_id = class_id

    print(student)

    db.session.add(student)
    db.session.commit()
    print('添加成功！' + student.__str__())
    return 0


def get_students() -> dict:
    primary_list = db.session.query(Student).all()
    data = dict()
    for index, stu in enumerate(primary_list):
        dic = dict()
        dic['sid'] = stu.sid
        dic['sno'] = stu.sno
        dic['sname'] = stu.sname
        dic['class'] = Class.get_class_name(stu.class_id)
        dic['queue'] = queue.get_queue_name(stu.queue_id)
        dic['grade'] = stu.grade

        data[index] = dic

    return data


def get_student_id_by_sno(sno: str) -> int:
    res = db.session.query(Student).filter_by(sno=sno).first()
    if res is None:
        return -1
    else:
        return res.sid


def get_student_info_by_sid(sid: str) -> dict:
    res = db.session.query(Student).filter_by(sid=sid).first()
    dic = dict()
    dic['sid'] = res.sid
    dic['sno'] = res.sno
    dic['sname'] = res.sname
    dic['grade'] = res.grade
    dic['class'] = Class.get_class_name(res.class_id)
    dic['queue'] = queue.get_queue_name(res.queue_id)

    return dic


def student_login(sno: str, password: str) -> int:
    res = db.session.query(Student).filter_by(sno=sno).first()
    if res is None:
        return -1
    elif res.password == password:
        return res.sid
    else:
        return -1


def get_grade_by_sid(sid: int):
    res = db.session.query(Student).filter_by(sid=sid).first()
    return res.grade
