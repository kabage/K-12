

def main():
    print "teacher's console"


if __name__=='__main__':
    main()

class PersonalDetails(object):

    def __init__(self):
        # gradelevel K-12
        # Teachers can have multiple students
        # There cant be any students if Teachers arent present
        
        self.gradeleveloptions=["kindergarten","G1","G2","G3","G4","G5","G6","G7","G8","G9","G10","G11","G12",]

        self._firstname= None
        self._secondname= None
        self._gradelevel= None

    @property
    def firstname(self):
        """ retrieves individual's first name """
        print "Get first name"
        return self._firstname

    @firstname.setter
    def firstname(self, firstname):
        """ sets an individual's first name """
        print "Set first name"
        self._firstname=firstname


    @property
    def secondname(self):
        """ A retrieves individual's second name """
        print "Get second name"
        return self._secondname

    @secondname.setter
    def secondname(self, secondname):
        """sets an individual's second name """
        print "Set second name"
        self._secondname=secondname

    @property
    def gradelevel(self):
        """ retrieves an individual's grade level"""
        print "Get grade level"
        return self._gradelevel

    @gradelevel.setter
    def gradelevel(self, gradelevel):
        """ sets an individual's gradelevel """
        print "Set grade level"
        self._gradelevel=gradelevel

