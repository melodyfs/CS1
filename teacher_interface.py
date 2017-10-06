import sys
import string
from student import Student
from classroom import Classroom


def ask():
    print("Welcome! Here's the list for commands:")
    print("Create new classroom - cr")
    print("Add new course - c")
    print("Add new student - s")

    command = raw_input("What do you want to do? ")

    if command == "cr":
        new_classroom = raw_input("Classroom name:")
        classroom = Classroom(new_classroom)
        print("Your classroom '%s' has been created!" % new_classroom)

    elif command == "add":
        new_course = raw_input("course name:")
        course_time = raw_input("course time:")
        classroom = Classroom(new_course,course_time)
        classroom.add_course()
        print("Added (%s, %s) to your course list!" % (new_course, course_time))

    else:
        print "Command not found"
        ask()


ask()
