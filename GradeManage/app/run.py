from flask import request, jsonify
from flask_cors import CORS, cross_origin
from app import app
from service import excel_service, user_service, control_service
import json

CORS(app, supports_credentials=True)
# 注册CORS, "/*" 允许访问所有api


@cross_origin(supports_credentials=True)
@app.route('/add_student', methods=['post'])
def upload_student():
    get = request.get_data()
    data = json.loads(get)
    errNum: int = excel_service.add_student_from_excel(data["data"])
    if errNum == 0:
        return {'status': 'ok'}
    else:
        return {
            'status': 'error',
            'errNum': errNum
        }


@cross_origin(supports_credentials=True)
@app.route('/faculty_login', methods=['post'])
def login_1():
    get = request.get_data()
    data = json.loads(get)
    worknumber: str = data["worknumber"]
    password: str = data["password"]
    res: str = user_service.faculty_login(worknumber, password)
    print(res)
    if res != "error":
        return {
            'status': 'ok',
            'privilege': res,
            'worknumber': worknumber
        }
    else:
        return {
            'status': 'error'
        }


@cross_origin(supports_credentials=True)
@app.route('/initData', methods=['get'])
def init_data():
    data1 = user_service.get_all_faculties()
    data2 = control_service.get_students()
    data3 = control_service.get_students_grades()
    data4 = control_service.get_all_class()
    data5 = control_service.get_all_queue()
    data = {
        'faculties': data1,
        'students': data2,
        'grades': data3,
        'class': data4,
        'queue': data5
    }
    return data


@cross_origin(supports_credentials=True)
@app.route('/add_course', methods=['post'])
def add_course():
    get = request.get_data()
    data = json.loads(get)
    control_service.add_course(data)
    return 'ok'


@cross_origin(supports_credentials=True)
@app.route('/add_faculty', methods=['post'])
def add_faculty():
    get = request.get_data()
    data = json.loads(get)
    res: int = control_service.add_faculty(data)
    if res == -1:
        return "error"
    else:
        return "ok"


@cross_origin(supports_credentials=True)
@app.route('/delete_user', methods=['post'])
def change_user():
    get = request.get_data()
    data = json.loads(get)
    control_service.delete_user(data['worknumber'])
    return 'ok'


@cross_origin(supports_credentials=True)
@app.route('/upload_grades', methods=['post'])
def upload_grades():
    get = request.get_data()
    data = json.loads(get)
    res = excel_service.upload_grades(data['file'], data['type'])
    return {
        'errNum': res
    }


@cross_origin(supports_credentials=True)
@app.route('/student_login', methods=['post'])
def stu_login():
    get = request.get_data()
    data = json.loads(get)
    sno = data['worknumber']
    password = data['password']
    res = user_service.student_login(sno, password)
    if res != -1:
        return {
            'status': 'ok',
            'privilege': 'student',
            'sid': res
        }
    else:
        return {
            'status': 'error'
        }


@cross_origin(supports_credentials=True)
@app.route('/grades_analyse', methods=['post', 'get'])
def analyse():
    get = request.get_data()
    data = json.loads(get)
    sid = data['sid']
    return control_service.analyse_for_all(sid)


@cross_origin(supports_credentials=True)
@app.route('/change_user_info', methods=['post'])
def change_user_info():
    get = request.get_data()
    data = json.loads(get)
    control_service.change_user_info(data)
    return 'ok'


@cross_origin(supports_credentials=True)
@app.route('/add_queue', methods=['post', 'get'])
def add_queue():
    get = request.get_data()
    data = json.loads(get)
    if control_service.add_queue(data) == 0:
        return 'ok'
    else:
        return 'error'


@cross_origin(supports_credentials=True)
@app.route('/change_queue', methods=['post', 'get'])
def change_queue():
    get = request.get_data()
    data = json.loads(get)
    if control_service.change_queue(data) == 0:
        return 'ok'
    else:
        return 'error'


@cross_origin(supports_credentials=True)
@app.route('/change_class', methods=['post', 'get'])
def change_class():
    get = request.get_data()
    data = json.loads(get)
    if control_service.change_class(data) == 0:
        return 'ok'
    else:
        return 'error'


@cross_origin(supports_credentials=True)
@app.route('/add_class', methods=['post', 'get'])
def add_class():
    get = request.get_data()
    data = json.loads(get)
    if control_service.add_class(data) == 0:
        return 'ok'
    else:
        return 'error'


if __name__ == '__main__':
    app.run()
