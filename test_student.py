from student import Student
# import pytest



def setup_for_test():
    student = Student("Yep", 1)
    return student

def test_init_student():
    student = Student("Yep", 1)
    assert student.name == "Yep"
    assert student.stuid == 1
    assert student.assignment == {}
    assert student.gpa == None

def test_add_assignment():
    student = setup_for_test()
    student.add_assignment('Hw1', 90)
    assert student.assignments['Hw1'] == 90
    student.add_assignment('Hw2', 120)
    assert student.assignments['Hw2'] == 120
    assert len(student.assignments) == 2

def test_delete_assignment():
    student = setup_for_test()
    student.add_assignment('Hw1', 90)
    student.add_assignment('Hw2', 120)
    student.delete_assignment('Hw1')
    assert len(student.assignments) == 1
    student.delete_assignment('Hw2')
    assert len(student.assignments) == 0

def test_update_assignment_grade():
    student = setup_for_test()
    student.add_assignment('Hw1', 90)
    student.add_assignment('Hw2', 120)
    student.update_assignment_grade('Hw1', 100)
    assert student.assignments['Hw1'] == 100

def test_calculate_gpa():
    student = setup_for_test()
    student.add_assignment('Hw1', 90)
    student.add_assignment('Hw2', 120)
    student.calculate_gpa()
    assert student.gpa == (90 + 120) / 2


setup_for_test()
test_init_student()
# test_add_assignment()
# test_delete_assignment
# test_calculate_gpa()
# test_update_assignment_grade()
test_show_student()
