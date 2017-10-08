import sys
from student import Student


class Classroom(Student):

    courses = {}
    assignments = {}


    def __init__(self, name):
        self.name = name
        self.time = None
        self.roster = {}

        #enroll students
    def enroll_student(self,stud_name, stud_id):
        student = Student(stud_name, stud_id)
        self.roster = student.add_student()

        return self.roster

    # give same assignment to each student
    def give_assignment(self, stud_id, new_hw, grade):
        new_assignment = Classroom.assignments
        student = Student.students
        stu_asgn = Student.assignments

        for i in self.roster.values():
            if i == stud_id:
                new_assignment[stud_id] = new_hw
                Student().add_assignment(grade)
                print(stud_id)
                print(new_assignment[stud_id])
                print(student.assignment)
                return new_assignment[stud_id]

        #view students

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




cs = Classroom("CS")
print(cs.add_course("python", "7-8am"))
print(cs.enroll_student("Newbie", 1))
print("---------")
print(cs.roster)
cs.give_assignment(1, "gradebook", 100)
print(cs.assignments)
# cs1 = Classroom("CS1", "")
# cs1.delete_course()
# print("-------")
# cs.show_student()
# cs.update_course_time("CS", "9-10am")
