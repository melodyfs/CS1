
class Student():

    students = {}
    assignments = {}

    def __init__(self, name, stuid):
        self.name = name
        self.assignment = {}
        self.gpa = None
        self.stuid = stuid

# Update student (CRUD)
    def add_student(self):
        student = Student.students
        student[self.name] = int(self.stuid)
        print student
        return student


    def delete_student(self):
        student = Student.students
        if self.name in student:
            student.pop(self.name, None)
            print(student)
            return student
        else:
            print "Name does not exist"

    def add_assignment(self, hw, grade):
        assignment = Student.assignments
        assignment[hw] = grade
        print assignment

        return assignment

    def delete_assignment(self, hw):
        assignment = Student.assignments
        if hw in assignment:
            assignment.pop(hw, None)
            print(assignment)
            return assignment
        else:
            print("No assignment found")

    def update_assignment_grade(self, hw, grade):
        assignment = Student.assignments
        if hw in assignment:
            assignment[hw] = grade
            print("Updated %s grade: %d" % (hw, grade))
            return assignment
        else:
            print("No assignment found")

    def calculate_gpa(self):
        assignment = Student.assignments
        gpa = sum(assignment.values()) / len(assignment)
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
# Student.add_student({"no":3})

# st.add_assignment("math", 3)
# st.delete_assignment("Eng")
# print("--------")
# st.update_assignment_grade("math", 50)

# Student.add_assignment({"Math": 3})
# print("Add assign. %s" % Student.assignments)


# Update assignment (CRUD)

# Get grades
