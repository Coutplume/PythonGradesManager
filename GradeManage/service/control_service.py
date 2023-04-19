from model import faculty, student, Grades, Class, queue
from collections import OrderedDict


def add_faculty(data):
    res: int = faculty.add_faculty(data['worknumber'],
                                    data['name'],
                                    data['password'],
                                   data['privilege'])
    return res


def change_user_info(data):
    faculty.change_user_info(data['worknumber'],
                             data['name'],
                             data['password'],
                             data['privilege'])
    return 0


def delete_user(worknumber):
    faculty.delete_user(worknumber)


def get_students() -> dict:
    return student.get_students()


# 获取所有的成绩记录
def get_students_grades() -> dict:
    primary_list = Grades.get_all_grades()
    data = dict()
    for index, grades in enumerate(primary_list):
        dic = student.get_student_info_by_sid(grades.sid)
        dic['grades'] = grades.grades
        dic['time'] = grades.time
        dic['grades_id'] = grades.grades_id
        temp: str = ''
        if grades.grades_type == 'study':
            temp = '学习成绩'
        elif grades.grades_type == 'second':
            temp = '第二课堂'
        elif grades.grades_type == 'exam':
            temp = '联考成绩'
        else:
            temp = '组织评价'
        dic['type_name'] = temp
        dic['type'] = grades.grades_type
        data[index] = dic
    return data


# 返回指定sid的各科目相关的成绩数据
def analyse_grade(sid: int) -> dict:
    grades_list = Grades.get_all_grades_by_id(sid)
    if grades_list is None:
        return {}
    data = dict()
    data['org'] = analyse_grades_by_type('org', grades_list)
    data['study'] = analyse_grades_by_type('exam', grades_list)
    data['second'] = analyse_grades_by_type('second', grades_list)
    data['exam'] = analyse_grades_by_type('exam', grades_list)
    return data


def analyse_grades_by_type(grades_type: str, grades_list: list) -> dict:
    total_mid: int = 0
    flag = 0
    data = dict()
    for index, grades in enumerate(grades_list):
        if grades.grades_type == grades_type:
            dic = dict()
            dic['time'] = grades.time
            dic['grades'] = grades.grades
            data[str(flag)] = dic
            flag += 1
            total_mid += int(grades.grades)
    if flag == 0:
        return {}
    data['score'] = total_mid/flag
    return data


def analyse_for_all(sid) -> dict:
    # target 为目标学生
    target = analyse_grade(sid)
    grade = student.get_grade_by_sid(sid)
    target['grade'] = grade
    stus = student.get_students()
    all_grades = dict()
    for key in stus:
        stu = stus[key]
        sid_temp = stu['sid']
        # 同一年级的才计算排名
        if stu['grade'] == grade:
            dic = analyse_grade(int(sid_temp))
            all_grades[sid_temp] = dic

    for key in all_grades:
        total = all_grades[key]['study']['score']*0.7 + all_grades[key]['org']['score']*0.3
        all_grades[key]['total'] = {
            'score': total
        }
        if key == sid:
            target['total'] = {
                'score': total
            }

    print(all_grades)

    temp = dict()
    temp = get_rank_and_avg(all_grades, 'org', sid)
    target['org']['rank'] = temp['rank']
    target['org']['avg'] = temp['avg']
    target['org']['name'] = '组织评价'
    temp = get_rank_and_avg(all_grades, 'second', sid)
    target['second']['rank'] = temp['rank']
    target['second']['avg'] = temp['avg']
    target['second']['name'] = '第二课堂'
    temp = get_rank_and_avg(all_grades, 'exam', sid)
    target['exam']['rank'] = temp['rank']
    target['exam']['avg'] = temp['avg']
    target['exam']['name'] = '联考成绩'
    temp = get_rank_and_avg(all_grades, 'study', sid)
    target['study']['rank'] = temp['rank']
    target['study']['avg'] = temp['avg']
    target['study']['name'] = '学习成绩'
    temp = get_rank_and_avg(all_grades, 'total', sid)
    target['total']['rank'] = temp['rank']
    target['total']['avg'] = temp['avg']
    target['total']['name'] = '总成绩'
    return target


def get_rank_and_avg(data: dict, grades_type: str, sid: int) -> dict:
    print(grades_type)
    rank: int = 1
    num: int = 0
    total: float = 0
    ordered = OrderedDict(sorted(data.items(), key=lambda i: i[1][grades_type]['score'], reverse=True))
    for key in ordered:
        num += 1
        total += float(ordered[key][grades_type]['score'])
        if key != sid:
            rank += 1
    if num == 0:
        return {
            'rank': rank,
            'avg': 0.0
        }
    else:
        return {
            'rank': rank,
            'avg': total/num
        }


def get_all_class() -> dict:
    res = Class.get_all_class()
    if res is None:
        return {}
    data = dict()
    for item in res:
        dic = dict()
        dic['class_id'] = item.class_id
        dic['class_name'] = item.class_name
        dic['tutor_id'] = item.tutor_id
        dic['queue_id'] = item.queue
        dic['queue_name'] = queue.get_queue_name(int(item.queue))
        dic['grade'] = item.grade
        dic['tutor_name'] = faculty.get_name(item.tutor_id)
        data[item.class_id] = dic

    return data


def get_all_queue() -> dict:
    res = queue.get_all_queue()
    if res is None:
        return {}
    data = dict()
    for item in res:
        dic = dict()
        dic['queue_id'] = item.queue_id
        dic['queue_name'] = item.queue_name
        dic['queue_grade'] = item.queue_grade
        dic['queue_cadre'] = item.queue_cadre
        dic['cadre_name'] = faculty.get_name(item.queue_cadre)
        data[item.queue_id] = dic
    return data


def add_queue(data) -> int:
    queue_name = data['queue_name']
    queue_grade = data['queue_grade']
    if queue.has_queue(queue_name, queue_grade):
        return -1
    queue_cadre = data['queue_cadre']
    queue.add_queue(queue_name=queue_name, queue_grade=queue_grade, queue_cadre=queue_cadre)
    return 0


def change_queue(data) -> int:
    queue_id = data['queue_id']
    queue_name = data['queue_name']
    queue_grade = data['queue_grade']
    if queue.has_queue(queue_name, queue_grade):
        return -1
    queue_cadre = data['queue_cadre']
    queue.change_queue(queue_id=queue_id, queue_name=queue_name, queue_grade=queue_grade, queue_cadre=queue_cadre)
    return 0


def change_class(data) -> int:
    class_id = data['class_id']
    class_name = data['class_name']
    grade = data['grade']
    if Class.has_class(class_name, grade):
        return -1
    tutor_id = data['tutor_id']
    queue_id = data['queue_id']
    Class.change_class(class_id=class_id, class_name=class_name, grade=grade, tutor_id=tutor_id, queue_id=queue_id)
    return 0


def add_class(data):
    class_name = data['class_name']
    grade = data['grade']
    if Class.has_class(class_name, grade):
        return -1
    tutor_id = data['tutor_id']
    queue_id = data['queue_id']
    Class.add_class(class_name, grade, tutor_id, queue_id)
    return 0