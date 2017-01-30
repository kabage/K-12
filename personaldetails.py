

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

        self._first_name= None
        self._second_name= None
        self._grade_level= None 

    @property
    def first_name(self):
        """ retrieves individual's first name """
        print "Get first name"
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """ sets an individual's first name """
        print "Set first name"
        self._first_name=first_name


    @property
    def second_name(self):
        """ A retrieves individual's second name """
        print "Get second name"
        return self._second_name

    @second_name.setter
    def second_name(self, second_name):
        """sets an individual's second name """
        print "Set second name"
        self._second_name=second_name

    @property
    def grade_level(self):
        """ retrieves an individual's grade level"""
        print "Get grade level"
        return self._grade_level

    @grade_level.setter
    def grade_level(self, grade_level):
        """ sets an individual's gradelevel """
        print "Set grade level"
        self._grade_level=grade_level

