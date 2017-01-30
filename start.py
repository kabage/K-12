import peewee

def main():
    print "K-12\n"

    school_name = raw_input("Enter School Name: \n")

    if school_name==None:
        print "School name can't be empty\n"
    else:
        database = peewee.SqliteDatabase(school_name+".db")

        print "\nSelected School is "+ school_name
        print "Please select an option\n"
        print "1. Create Student Record"
        print "2. Create Teacher Record"


        selected_operation = raw_input("\nOperation: \n")

        if selected_operation=="1":
            print "create student record"
        elif selected_operation=="2":
            print "create teacher record"
        else:
            print "Operation not supported"

def create_student_record(school_name):
    pass

def create_teacher_record(school_name):
    pass



if __name__=='__main__':
    main()

