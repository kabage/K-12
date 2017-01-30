from personaldetails import PersonalDetails
import peewee

def main():
    print "running as standalone"

if __name__ == '__main__':
    main()

school_name="SCHOOLX"
database = peewee.SqliteDatabase(school_name+".db")

class Student(peewee.Model):

    first_name= peewee.CharField()
    second_name= peewee.CharField()
    grade_level= peewee.CharField()
    teacher_name=peewee.CharField()  

    class Meta:
        database=database   

class StudentDetails(PersonalDetails):

    def __init__(self):
        # gradelevel K-12
        # Students have a gpa. Out of a hundred
        # There can't be any students if Teachers arent present
        PersonalDetails.__init__(self)
        self._gpa = None
        self._teacher_name = None

    @property
    def gpa(self):
        """ retrieves student gpa"""
        print "Get gpa"
        return self._gpa

    @gpa.setter
    def gpa(self, gpa):
        """ sets student gpa"""
        print "Set gpa"
        self._gpa=gpa
      

    @property
    def teacher_name(self):
       """ retrieves student teacher name"""
       print "Get student teacher name"
       return self._teacher_name

    @teacher_name.setter
    def teacher_name(self, teacher_name):
       """ sets student teacher name"""
       print "Set student teacher name"
       self._teacher_name=teacher_name

    def save_details(self):

      database.connect()
      try:
        Student.create_table()
      except peewee.OperationalError, e:
        print "table exists "+e.message
      else:
        print "table created succcessfully"
      finally:
        student_object= Student(first_name=self.first_name,second_name=self.second_name,grade_level=self.grade_level,teacher_name=self.teacher_name)
        student_object.save()
        
            
      

student_details=StudentDetails()
student_details.first_name="sfs5df"
student_details.second_name="sf5df"
student_details.grade_level="rgw5rgr"
student_details.teacher_name="rgwr5gr"
student_details.save_details()
