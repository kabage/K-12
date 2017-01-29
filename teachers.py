from personaldetails import PersonalDetails
from peewee import *

def main():
    print "teacher's console"


if __name__=='__main__':
    main()


class Teachers(PersonalDetails):
    
    def __init__(self):
        PersonalDetails.__init__(self)
        self.students=None
    
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

    def savedetails():
        pass



teacherobject = Teachers()
print teacherobject.firstname

teacherobject.secondname="bup"
print teacherobject.secondname

teacherobject.gradelevel=6
print teacherobject.gradelevel

print teacherobject.students

