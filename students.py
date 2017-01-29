
from personaldetails import PersonalDetails


def main():
    print "running as standalone"

if __name__ == '__main__':
    main()


class Students(PersonalDetails):

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
       return self._teachername

    @teachername.setter
    def teacher_name(self, teacher_name):
       """ sets student teacher name"""
       print "Set student teacher name"
       self._teachername=teacher_name

    def savedetails():
      pass

