# K-12
This is a tool that helps generate a K-12 school with students and teachers at every grade level.
## How to use.
K-12 has one external dependancy .ie peewee as an orm for the sqlite database. http://docs.peewee-orm.com/en/latest/
To run K-12, install this dependacy and run start.py.
## Adding Records.
When you run start.py, a console starts  prompting you to enter the school name.
Type this in as it cannot be null. After the school name select an option for adding records.ie as a teacher or student, by typing 1 or 2.

Adding teachers is straight forward as you only need to type the personal details as prompted. The grade can only be either  k,g1,g2,g3,g4,g5,g6,g7,g8,g9,g10,g11,or g12

When adding students records, the teachers table cannot be empty and the grade selected must have a teacher.

## Database Structure.
1. Your school should have a name, and can have many students and many teachers.
2. Students have names, GPAs (out of 100), grade level (K - 12), and a teacher name.
3. Teachers have names and grade levels, and should be able to have multiple students.
4. A teacher should have no more than 10 students.
5. If there are no teachers, there should be no students.
6. There is a ***one to many relationship*** between teachers and students.

## Code Structure.
### 1. personaldetails.py

**PersonalDetails** - This class contains getters and setters for individual details.ie both students and teachers.

first_name
second_name
grade_level
school_name

### 2. students.py
**Student** - This is the db model for students.
**StudentDetails** - Inherits shared attributes from PersonalDetails
-Contains getters and setters for student details.
-**save_details** - Contains code to connect to database and save student objects.
-**student_count** - Query to ensure the teacher has a student count of less than 10 before assigning new student

### 3. teachers.py
**Teacher** - This is the db model for teachers.
**TeacherDetails** - Inherits shared attributes from PersonalDetails.
**teachers_exist** - Query checks if teachers exist.
**save_details** - Contains code to connect to database and save teacher objects.
**teachers_in_grade** - Query returns the teachers in a particular grade.

### 4. start.py
**main** - This is the program entry point.
It calls the functions relating to user input and data read/write.
**create_teacher_record** - saves teacher data from user, takes in **personal_details** as an argument, populates a **TeachersDetails** object and saves it.
**create_student_record** -Populates student model and validates student data.
**save_student_record** - Populates a StudentDetails objects and saves student record to database.
**get_personal_details**-Prompts user to enter the basic details for teachers and students.
**input_valid** - Ensures user input is not null.
**grade_is_valid** - Ensures the grade entered is between kindergarten and g12.




