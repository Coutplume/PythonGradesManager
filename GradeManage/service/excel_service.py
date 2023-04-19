from util.deconder import deconder
from model import student, Grades


def add_student_from_excel(data: str) -> int:
    strs = data.split(";")[1].split(",")
    dic = deconder(strs[1])
    print(dic)
    snos: dict = dic['学号']
    snames: dict = dic['姓名']
    class_names: dict = dic['教学班']
    grades: dict = dic['年级']
    queue_names: dict = dic['学员队']
    length = snos.__len__()
    num: int = 0
    for index in range(length):
        try:
            res = student.add_student(sno=snos[index], sname=snames[index], class_name=class_names[index],
                                      grade=grades[index], queue_name=queue_names[index])
            if res == -1:
                num += 1
        except BaseException:
            num += 1
        finally:
            continue
    print(num)
    return num


def upload_grades(data: str, grades_type: str) -> int:
    strs = data.split(";")[1].split(",")
    dic = deconder(strs[1])
    print(dic)
    snos: dict = dic['学号']
    time: dict = dic['学年']
    grades: dict = dic['成绩']
    length = snos.__len__()
    errNum: int = 0
    for index in range(length):
        sid = student.get_student_id_by_sno(snos[index])
        res = Grades.add_grade(sid=sid, time=time[index], grades=grades[index], grades_type=grades_type)
        if res == -1:
            errNum += 1
    return errNum
