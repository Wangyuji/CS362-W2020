from unittest import TestCase
import classroom_manager as room


class TestStudent(TestCase):
    def setUp(self):
        self.student = room.Student(933,"Yujie", "Wang")
        self.assignment = room.Assignment("Assignment4", 100)

    def test_init(self):
        self.assertEqual(self.student.id, 933)
        self.assertEqual(self.student.first_name, "Wang")
        self.assertEqual(self.student.last_name, "Yujie")
        self.assertEqual(self.student.assignments, [])

    def test_full_name(self):
        self.assertEqual(self.student.get_full_name(), "Wang,Yujie")

    def test_submit_assignment(self):
        self.assertEqual(0, len(self.student.assignments))
        self.student.submit_assignment(self.assignment)
        self.assertEqual(2, len(self.student.assignments))

    def test_get_assignment(self):
        #initialize variable 
        self.assignment2 = room.Assignment("Assignment2", 98)

        #call function
        self.student.submit_assignment(self.assignment)
        self.student.submit_assignment(self.assignment2)
        self.assertEqual(self.student.assignments, self.student.get_assignments())
    

    def test_get_assignments(self):
        self.student.submit_assignment(self.assignment)
        assert self.student.get_assignment(self.assignment.name).name == "Assignment4"


    def test_get_average(self):
        assignment2 = room.Assignment('Assignment2', 101)
        assignment2.grade = 100
        assignment3 = room.Assignment('Assignment3', 101)
        assignment3.grade = 98

        self.student.submit_assignment(assignment2)
        self.student.submit_assignment(assignment3)
        #avg = (100+98) / 2 = 99
        avg = 99
        self.assertEqual(avg, self.student.get_average())


    def test_remove_assignment(self):
        assignment2 = room.Assignment("Assignment2", 101)
        assignment3 = room.Assignment("Assignment3", 101)
        self.student.submit_assignment(assignment2)
        self.student.submit_assignment(assignment3)

        self.student.remove_assignment('Assignment2')
        #There are 3 name and 3 max score in in the string
        #so the total is 6, after roming one with calling fucniton
        #the length become 4
        self.assertEqual(4, len(self.student.assignments))

class TestAssignment(TestCase):
    def setUp(self):
        self.assignment = room.Assignment("Assignment4", 100)

    def test_init(self):
        self.assertEqual(self.assignment.name, "Assignment4")
        self.assertEqual(self.assignment.max_score, 100)
        self.assertEqual(self.assignment.grade, None)

    def test_assign_grade(self):
        self.assignment.assign_grade(10)
        assert self.assignment.grade == 10
        self.assignment.assign_grade(110)
        self.assertIsNone(self.assignment.grade)





        



