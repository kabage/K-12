import peewee
from teachers import *
from students import *
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
            create_student_record()

        elif selected_operation=="2":
            print "create teacher record"
            try:
                create_teacher_record(get_personal_details())
            except TypeError, e:
                print "Input Invalid "+"Missing field"
        else:
                print "Operation not supported"    

def create_teacher_record(personal_details):

    teacher_details=TeacherDetails()
    teacher_details.first_name=personal_details[0]
    teacher_details.second_name=personal_details[1]
    teacher_details.grade_level=personal_details[2]
    teacher_details.save_details()

def create_student_record():
    teacher_details=TeacherDetails()

    if teacher_details.teachers_exist:

        print "teachers exist"
        student_details=StudentDetails()
        student_details.first_name="A"
        student_details.second_name="A"
        student_details.grade_level="A"
        student_details.gpa=99
        student_details.teacher_object=Teacher.select().get()
        student_details.save_details()

    else:
        print "Teachers unavailable"


def get_personal_details():

    personal_details=[]

    first_name = raw_input("Enter first name: \n")
    if input_valid(first_name):
        second_name= raw_input("Enter second Name: \n")
        if input_valid(second_name):
            grade_level=raw_input("Enter grade level: \n")

            if input_valid(grade_level):
                personal_details.append(first_name)
                personal_details.append(second_name)
                personal_details.append(grade_level)
                return personal_details

            else:   
                return None
        else:   
            return None
    else:
        return None

    

def input_valid(value):
    if len(value) ==0 or value==None:
        print "Value is invalid"
        return False
    else:
        return True
        


if __name__=='__main__':
    main()

