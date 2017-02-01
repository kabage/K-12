import peewee
from personaldetails import PersonalDetails

def main():
    print ""


if __name__ == '__main__':
    main()

school_name="school"
database = peewee.SqliteDatabase(school_name + ".db")

class Teacher(peewee.Model):
    """This class defines the teacher database model"""
    # gradelevel K-12
    # Teachers can have multiple students
    # There cant be any students if Teachers arent present

    first_name = peewee.CharField()
    second_name = peewee.CharField()
    grade_level = peewee.CharField()
    school_name=peewee.CharField()

    class Meta:
        database = database


class TeacherDetails(PersonalDetails):
    """TeachersDetails inherits the basic fields from PersonalDetails"""
    def __init__(self):

        self._students = None

        PersonalDetails.__init__(self)

    def teachers_exist(self):
        """Query checks if teachers exist"""
        if Teacher.table_exists():
            teachers_available = Teacher.select().count()
            print teachers_available
            if teachers_available > 0:
                return True
            else:
                return False
        else:
            return False

    def save_details(self):
        """Saves teacher details to the database"""
        database.connect()
        try:
            Teacher.create_table()
        except peewee.OperationalError, e:
            print "table found " + e.message
        else:
            print "table created successfully"
        finally:
            teacher_object = Teacher(
                first_name=self.first_name, second_name=self.second_name, grade_level=self.grade_level,school_name=self.school_name)
            teacher_object.save()
            print "Record saved"


    def teachers_in_grade(self, grade_level):
        """Query returns the teachers in a particular grade"""
        teachers_in_grade = []
        for teacher in Teacher.select().where(Teacher.grade_level == grade_level):
            teachers_in_grade.append(teacher)

        return teachers_in_grade
