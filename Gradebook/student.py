

class Student():

    students = {}
    assignments_grades = {}

    def __init__(self, name, stuid):
        self.name = name
        self.assignment_grades = {}
        self.gpa = None
        self.stuid = stuid

# Update student (CRUD)
    def add_student(self):
        student = Student.students
        student[self.name] = int(self.stuid)
        # print student
        return student


    def delete_student(self):
        student = Student.students
        if self.name in student:
            student.pop(self.name, None)
            print(student)
            return student
        else:
            print "Name does not exist"

    def add_assignment(self, stud_id, new_hw):
        new_assignment = Student.assignments_grades

        # initiate a new object if the student has never been given an assignment
        if stud_id not in new_assignment:
            new_assignment[stud_id] = {}
            new_assignment[stud_id].update({new_hw: 0})
            print(new_assignment)
        # else insert a new dict into exsiting object
        else:
            new_assignment[stud_id].update({new_hw: 0})
            print(new_assignment)


    def delete_assignment(self, stud_id, hw):
        assignment = Student.assignments_grades
        the_assignment = assignment[stud_id]
        if hw in the_assignment:
            the_assignment.pop(hw, None)
            print(the_assignment)
        else:
            print("No assignment found")

    def update_assignment_grade(self, stud_id, hw, grade):
        assignment = Student.assignments_grades
        the_assignment = assignment[stud_id]
        if hw in the_assignment:
            the_assignment[hw] = grade
            print("Updated %s grade: %d" % (hw, the_assignment[hw]))
            return assignment
        else:
            print("No assignment found")

    def calculate_gpa(self, stud_id):
        assignment_grades = Student.assignments_grades[stud_id]
        gpa = sum(assignment_grades.values()) / len(assignment_grades)
        self.gpa = gpa

        print(self.gpa)
        return self.gpa

    def show_student(self):
        student = Student.students
        print student


# st = Student("you", 1)
# st.add_student()
# st2 = Student("no", 2)
# st2.add_student()
#
# st.add_assignment(2, "Chem")
# # st.delete_assignment(2, "Chem")
# st.add_assignment(2, "Math")
#
# print("-------")
# print(st.assignments_grades)
# print("--------")
# st.update_assignment_grade(2, "Chem", 50)

# Student.add_assignment({"Math": 3})
# print("Add assign. %s" % Student.assignments)

# st.calculate_gpa(2)

# Update assignment (CRUD)

# Get grades
