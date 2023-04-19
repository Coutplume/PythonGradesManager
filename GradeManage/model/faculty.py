from app import db


class Faculty(db.Model):
    __tablename__ = 'faculty'
    worknumber = db.Column(db.String(255), primary_key=True)
    name = db.Column(db.String(10), unique=False)
    password = db.Column(db.String(255), unique=False)
    privilege = db.Column(db.String(80), unique=False)

    def __init__(self, worknumber, name, password, privilege):
        self.worknumber = worknumber
        self.name = name
        self.password = password
        self.privilege = privilege

    def __str__(self):
        return "{} {} {} {}".format(self.worknumber, self.name, self.password, self.privilege)


def faculty_login(worknumber: str, password: str) -> str:
    try:
        faculty = db.session.query(Faculty).filter_by(worknumber=worknumber).first()
        if faculty.password is password:
            return faculty.privilege
        else:
            return "error"
    except Exception:
        return "error"


def get_all_faculties():
    faculties = db.session.query(Faculty).all()
    return faculties


def add_faculty(worknumber, name, password, privilege):
    query = db.session.query(Faculty).filter_by(worknumber=worknumber).first()
    if query is not None:
        return -1
    faculty = Faculty(worknumber, name, password, privilege)
    db.session.add(faculty)
    db.session.commit()
    return 0


def change_user_info(worknumber, name, password, privilege):
    faculty = db.session.query(Faculty).filter_by(worknumber=worknumber).first()
    print(password)
    faculty.name = name
    faculty.password = password
    faculty.privilege = privilege
    db.session.add(faculty)
    db.session.commit()


def delete_user(worknumber):
    faculty = db.session.query(Faculty).filter_by(worknumber=worknumber).first()
    db.session.delete(faculty)
    db.session.commit()


def get_name(worknumber):
    faculty = db.session.query(Faculty).filter_by(worknumber=worknumber).first()
    return faculty.name
