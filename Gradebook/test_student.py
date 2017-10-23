from student import Student
# import pytest



def setup_for_test():
    student = Student("Yep", 1)
    return student

def test_init_student():
    student = Student("Yep", 1)
    assert student.name == "Yep"
    assert student.stuid == 1
    assert student.assignment_grades == {}
    assert student.gpa == None

def test_add_assignment():
    student = setup_for_test()
    student.add_assignment(1, 'Hw1')
    assert student.assignments_grades[1]['Hw1'] == 0
    student.add_assignment(1, 'Hw2')
    assert student.assignments_grades[1]['Hw2'] == 0
    assert len(student.assignments_grades[1]) == 2

def test_delete_assignment():
    student = setup_for_test()
    student.add_assignment(1, 'Hw1')
    student.add_assignment(1, 'Hw2')
    student.delete_assignment(1, 'Hw1')
    assert len(student.assignments_grades[1]) == 1
    student.delete_assignment(1, 'Hw2')
    assert len(student.assignments_grades[1]) == 0

def test_update_assignment_grade():
    student = setup_for_test()
    student.add_assignment(1, 'Hw1')
    student.add_assignment(1, 'Hw2')
    student.update_assignment_grade(1, 'Hw1', 100)
    assert student.assignments_grades[1]['Hw1'] == 100

def test_calculate_gpa():
    student = setup_for_test()
    student.add_assignment('Hw1', 90)
    student.add_assignment('Hw2', 120)
    student.calculate_gpa()
    assert student.gpa == (90 + 120) / 2


setup_for_test()
test_init_student()
# test_add_assignment()
test_delete_assignment
# test_calculate_gpa()
# test_update_assignment_grade()
# test_show_student()
