import sys
from student import Student


class Classroom():

    courses = {}

    def __init__(self, name):
        self.name = name
        self.time = None
        self.course = {}

    def add_course(self, course_name, time):
        course = Classroom.courses
        course[course_name] = time

        return course

    def delete_course(self, course_name):
        course = Classroom.courses
        if course_name in course:
            course.pop(course_name, None)
            return course
        else:
            print "Course does not exist"

    def update_course_time(self, course_name, time):
        course = Classroom.courses
        if course_name in course:
            course[course_name] = time
            print ("Updated %s time: %s" % (course_name, time))
            return course
        else:
            print("No course found")

    

# cs = Classroom("CS")
# print(cs.add_course("python", "7-8am"))
# cs1 = Classroom("CS1", "")
# cs1.delete_course()
# print("-------")
# cs.show_student()
# cs.update_course_time("CS", "9-10am")
