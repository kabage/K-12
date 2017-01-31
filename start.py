import peewee
from teachers import *
from students import *


def main():

    """program entry point"""
    print "K-12\n"

    school_name = raw_input("Enter School Name: \n")

    if school_name == None:
        print "School name can't be empty\n"
    else:
        database = peewee.SqliteDatabase(school_name + ".db")

        print "\nSelected School is " + school_name
        print "Please select an option\n"
        print "1. Create Student Record"
        print "2. Create Teacher Record"

        selected_operation = raw_input("\nOperation: \n")

        if selected_operation == "1":
            print "create student record"
            create_student_record(get_personal_details())

        elif selected_operation == "2":
            print "create teacher record"
            try:
                create_teacher_record(get_personal_details())
            except TypeError, e:
                print "Input Invalid " + "Missing field"
        else:
            print "Operation not supported"


def create_teacher_record(personal_details):
    """saves teacher data from user, parsed from personal_details"""
    teacher_details = TeacherDetails()
    teacher_details.first_name = personal_details[0]
    teacher_details.second_name = personal_details[1]
    teacher_details.grade_level = personal_details[2]
    teacher_details.save_details()


def create_student_record(personal_details):
    """populates student model and validates student data"""
    teacher_details = TeacherDetails()
    teachers_exist=teacher_details.teachers_exist()
    if teachers_exist:
        teachers_in_grade = teacher_details.teachers_in_grade(
            personal_details[2])
        if len(teachers_in_grade) == 0:
            print "Record not created. No teachers available for this grade"
        else:
            print "\n These teachers are available for this grade, choose one:\n"
            for index, teacher in enumerate(teachers_in_grade):
                print str(index)+". "+teacher.first_name+" "+teacher.second_name
            complete_student_record(teachers_in_grade,personal_details)  
           
    else:
        print "Teachers unavailable. Record cannot be created "

def complete_student_record(teachers_in_grade,personal_details):
    teacher_position = raw_input("Enter teacher index: \n")
    selected_teacher = teachers_in_grade[int(teacher_position)]
    if input_valid(teacher_position):
        gpa = raw_input("Enter GPA: \n")

        student_details = StudentDetails()
        teacher_available=student_details.student_count(personal_details[2], selected_teacher.id)
        if teacher_available:
            save_student_record(personal_details, selected_teacher,gpa)
        else:
            print "Record not created. Teacher already has 10 students."

def save_student_record(personal_details, selected_teacher,gpa):
    """saves student record to database"""
    student_details=StudentDetails()
    student_details.first_name = personal_details[0]
    student_details.second_name = personal_details[1]
    student_details.grade_level = personal_details[2]
    student_details.gpa = int(gpa)
    student_details.teacher_object = selected_teacher
    student_details.save_details()


def get_personal_details():
    """Prompts user to enter the basic details for teachers and students"""
    personal_details = []

    first_name = raw_input("Enter first name: \n")
    if input_valid(first_name):
        second_name = raw_input("Enter second Name: \n")
        if input_valid(second_name):
            grade_level = raw_input("Enter grade level: \n")

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
    """Ensures user input is not null"""
    if len(value) == 0 or value == None:
        print "Value is invalid"
        return False
    else:
        return True


if __name__ == '__main__':
    main()
