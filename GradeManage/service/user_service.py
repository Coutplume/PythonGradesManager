from model import faculty, student


def faculty_login(worknumber: str, password: str) -> str:
    return faculty.faculty_login(worknumber, password)


def get_all_faculties():
    res = faculty.get_all_faculties()
    data = dict()
    for index, item in enumerate(res):
        dic = dict()
        dic['worknumber'] = item.worknumber
        dic['name'] = item.name
        dic['privilege'] = item.privilege
        dic['password'] = item.password
        data[index] = dic
    return data


def student_login(sno: str, password: str) -> int:
    return student.student_login(sno, password)

