import sys
from student import Student


class Classroom(Student):

    courses = {}

    def __init__(self, name):
        self.name = name
        self.time = None
        self.roster = {}

        #enroll students

    def enroll_student(self, stud_name, stud_id):
        student = Student(stud_name, stud_id)
        self.roster = student.add_student()

        return self.roster

    #pass assignment to a student with the default grade 0
    def give_assignment(self, stud_id, new_hw):
        student = Student(self.roster, stud_id)
        student.add_assignment(stud_id, new_hw)

    # update the grade once the student complete the assignment
    def edit_grade(self, stud_id, hw, final_grade):
        student = Student(self.roster, stud_id)
        student.update_assignment_grade(stud_id, hw, final_grade)


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
# cs.enroll_student("Newbie", 1)
# cs.give_assignment(1, "Read")
#
# # print(cs.assignments[1])
# print("---------")
# print(cs.roster)
# cs.edit_grade(1, "Read", 130)
# print(cs.assignments[1]["Read"])


# cs.give_assignment(1, "gradebook", 100)
# print(cs.assignments)
# cs1 = Classroom("CS1", "")
# cs1.delete_course()
# print("-------")
# cs.show_student()
# cs.update_course_time("CS", "9-10am")
