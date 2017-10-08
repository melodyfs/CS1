from classroom import Classroom


def setup_for_test():
    classroom = Classroom("Music")
    return classroom

def test_init_class():
    classroom = Classroom("Music")
    assert classroom.name == "Music"

def test_add_course():
    classroom = setup_for_test()
    classroom.add_course("Violin", "1-3pm")
    classroom.add_course("Piano", "4-7pm")
    assert classroom.courses['Violin'] == "1-3pm"
    assert classroom.courses['Piano'] == "4-7pm"
    assert len(classroom.courses) == 2

def test_delete_course():
    classroom = setup_for_test()
    classroom.add_course("Violin", "1-3pm")
    classroom.add_course("Piano", "4-7pm")
    classroom.delete_course("Violin")
    assert len(classroom.courses) == 1
    classroom.delete_course("Piano")
    assert len(classroom.courses) == 0

def test_update_course_time():
    classroom = setup_for_test()
    classroom.add_course("Violin", "1-3pm")
    classroom.add_course("Piano", "4-7pm")
    classroom.update_course_time("Violin", "8-10am")
    assert classroom.courses["Violin"] == "8-10am"



test_init_class()
# test_add_course()
# test_delete_course()
