from personaldetails import PersonalDetails
import peewee
from teachers import Teacher


def main():
    print ""

if __name__ == '__main__':
    main()

school_name ="school"
database = peewee.SqliteDatabase(school_name + ".db")


class Student(peewee.Model):
    """The student has 4 fields. There's a one to many relationship between teachers and students"""
    first_name = peewee.CharField()
    second_name = peewee.CharField()
    grade_level = peewee.CharField()
    school_name=peewee.CharField()

    gpa = peewee.IntegerField()
    teacher = peewee.ForeignKeyField(Teacher, related_name='students')

    class Meta:
        database = database


class StudentDetails(PersonalDetails):
    """student inherits basic individual attribute from PersonalDetails"""

    def __init__(self):
        # gradelevel K-12
        # Students have a gpa. Out of a hundred
        # There can't be any students if Teachers arent present
        PersonalDetails.__init__(self)
        self._gpa = None
        self._teacher_object = None

    @property
    def gpa(self):
        """ retrieves student gpa"""
        return self._gpa

    @gpa.setter
    def gpa(self, gpa):
        """ sets student gpa"""   
        self._gpa = gpa

    @property
    def teacher_object(self):
        """ retrieves student teacher name"""
        return self._teacher_object

    @teacher_object.setter
    def teacher_object(self, teacher):
        """ sets student teacher name"""
        self._teacher_object = teacher

    def save_details(self):
        """saves student data to database"""
        database.connect()
        try:
            Student.create_table()
        except peewee.OperationalError, e:
            print "table found " + e.message
        else:
            print "table created succcessfully"
        finally:

            student_object = Student(first_name=self.first_name, second_name=self.second_name,
                                     grade_level=self.grade_level, gpa=self.gpa, teacher=self.teacher_object,school_name=self.school_name)
            student_object.save()
            print "Record Saved"

    def student_count(self, grade_level, teacher_id):
        """Query ensures the teacher has a student count of less than 10 before assigning new student"""
        if Student.table_exists()==False:
          Student.create_table()
        student_count = Student.select().where(Student.grade_level == grade_level).where(
            Student.teacher_id == teacher_id).count()
        if student_count < 10:
            return True

        else:
            return False
