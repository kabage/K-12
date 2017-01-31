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
     

    class Meta:
        database=database    


class TeacherDetails(PersonalDetails):


    def __init__(self):

        self._students=None
        

        PersonalDetails.__init__(self)

    def teachers_exist(self):
        teachers_available=Teacher.select()
        if len(teachers_available) >0:
            return True
        else:
            return False
    
    def save_details(self):

        database.connect()
        try:
            Teacher.create_table()
        except peewee.OperationalError, e:
            print "table exists "+ e.message
        else:
            print "table created successfully"    
        finally:
            teacher_object= Teacher(first_name=self.first_name,second_name=self.second_name,grade_level=self.grade_level)
            teacher_object.save()

    def retrieve_all_teacher_details(self):
        for teacher in Teacher.select().where(Teacher.first_name == 'edward'):
            print teacher.second_name

    def teachers_in_grade( self, grade_level):

        teachers_in_grade=[]
        for teacher in Teacher.select().where(Teacher.grade_level == grade_level):
            teachers_in_grade.append((Teacher.id,teacher.first_name,teacher.second_name))
            
        return teachers_in_grade


