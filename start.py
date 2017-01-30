import peewee
from teachers import *
import sys

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
            create_teacher_record("dfgrgf")
        else:
            print "Operation not supported"

def create_student_record(school_name):
    
    pass

def create_teacher_record(school_name):

    first_name = raw_input("Enter first name: \n")
    if input_valid(first_name):
        second_name= raw_input("Enter second Name: \n")
        if input_valid(second_name):
            grade_level=raw_input("Enter grade level: \n")
            if input_valid(grade_level):

                teacher_details=TeacherDetails()
                teacher_details.first_name=first_name
                teacher_details.second_name=second_name
                teacher_details.grade_level=grade_level
                teacher_details.save_details()

            else:
                print "Input invalid"
        else:
            print "Input invalid"
    else:
        print "Input invalid"

    

def input_valid(value):
    if len(value) ==0 or value==None:
        print "Value is invalid"
        return False
    else:
        return True
        


if __name__=='__main__':
    main()

