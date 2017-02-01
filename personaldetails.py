def main():
    print ""


if __name__ == '__main__':
    main()


class PersonalDetails(object):

    def __init__(self):
        # gradelevel K-12
        # Teachers can have multiple students
        # There cant be any students if Teachers arent present

        self.grade_level_options = ["k", "g1", "g2", "g3",
                                  "g4", "g5", "g6", "g7", "g8", "g9", "g10", "g11", "g12", ]

        self._first_name = None
        self._second_name = None
        self._grade_level = None
        self._school_name=None


    @property
    def first_name(self):
        """ retrieves individual's first name """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """ sets an individual's first name """
        self._first_name = first_name

    @property
    def second_name(self):
        """ A retrieves individual's second name """
        return self._second_name

    @second_name.setter
    def second_name(self, second_name):
        """sets an individual's second name """
        self._second_name = second_name

    @property
    def grade_level(self):
        """ retrieves an individual's grade level"""
        return self._grade_level

    @grade_level.setter
    def grade_level(self, grade_level):
        """ sets an individual's gradelevel """
        self._grade_level = grade_level
    
    @property
    def school_name(self):
        """ retrieves an individual's grade level"""
        return self._school_name

    @school_name.setter
    def school_name(self, school_name):
        """ sets an individual's gradelevel """
        self._school_name = school_name
