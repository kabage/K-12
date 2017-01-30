import peewee
from personaldetails import PersonalDetails
def main():
    print "teacher's console"


if __name__=='__main__':
    main()

school_name="SCHOOLX"
database = peewee.SqliteDatabase(school_name+".db")

class Teacher(peewee.Model):
    
    # gradelevel K-12
    # Teachers can have multiple students
    # There cant be any students if Teachers arent present

    first_name= peewee.CharField()
    second_name= peewee.CharField()
    grade_level= peewee.CharField()
    students=peewee.CharField()  

    class Meta:
        database=database    


class TeacherDetails(PersonalDetails):

    def __init__(self):

        self._students=None
        PersonalDetails.__init__(self)

    @property
    def students(self):
        """ retrieves students assigned to a teacher"""
        print "Get students"
        return self._students

    @students.setter
    def students(self, students):
        """ sets students to be assigned to teacher"""
        print "Set students"
        self._students=students
    
    
    def  save_details(self):

        database.connect()
        try:
            Teacher.create_table()
        except peewee.OperationalError, e:
            print "table exists "+ e.message
        else:
            print "table created successfully"    
        finally:
            teacher_object= Teacher(first_name=self.first_name,second_name=self.second_name,grade_level=self.grade_level,students=self.students)
            teacher_object.save()
    
teacher_details=TeacherDetails()
teacher_details.students="dfgerg"
teacher_details.first_name="sfsdf"
teacher_details.second_name="sfdf"
teacher_details.grade_level="rgwrg666r"
teacher_details.save_details()

