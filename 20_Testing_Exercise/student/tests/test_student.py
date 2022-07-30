from project.student import Student
from unittest import TestCase, main


class TestStudent(TestCase):
    def setUp(self) -> None:
        self.student = Student('Tanya', {'OOP': ['encapsulation', 'inheritance', 'polymorphism', 'abstraction'],
                                         'Algorithms': ['Graphs', 'DFS', 'BFS']})

    def test_init__set_attr_name(self):
        self.assertEqual('Tanya', self.student.name)

    def test_init__set_attr_cources(self):
        self.assertEqual({'OOP': ['encapsulation', 'inheritance', 'polymorphism', 'abstraction'],
                          'Algorithms': ['Graphs', 'DFS', 'BFS']}, self.student.courses)

    def test_init__set_attr_courses__when_courses_is_None(self):
        student = Student('Tanya')
        self.assertEqual({}, student.courses)

    def test_enroll__when_course_is_already_in_courses__expect_to_append_notes(self):
        result = self.student.enroll('OOP', ['error handling', 'testing', 'SOLID'], 'Y')
        self.assertEqual("Course already added. Notes have been updated.", result)
        self.assertEqual(['encapsulation', 'inheritance', 'polymorphism', 'abstraction','error handling', 'testing', 'SOLID'], self.student.courses['OOP'])

    def test_enroll_when_course_is_not_in_cources__and_add_notes_is_Y__expect_to_add_course_and_notes(self):
        result = self.student.enroll('Python OOP', ['error handling', 'testing', 'SOLID'], 'Y')
        self.assertEqual("Course and course notes have been added.", result)
        self.assertEqual({'OOP': ['encapsulation', 'inheritance', 'polymorphism', 'abstraction'],
                          'Algorithms': ['Graphs', 'DFS', 'BFS'],'Python OOP': ['error handling', 'testing', 'SOLID']}, self.student.courses)

    def test_enroll_when_course_is_not_in_cources__and_add_notes_is_N__expect_to_add_course_and_notes(self):
        result = self.student.enroll('Python OOP', ['error handling', 'testing', 'SOLID'], 'N')
        self.assertEqual("Course has been added.", result)
        self.assertEqual({'OOP': ['encapsulation', 'inheritance', 'polymorphism', 'abstraction'],
                          'Algorithms': ['Graphs', 'DFS', 'BFS'], 'Python OOP': []},
                         self.student.courses)

    def test_add_notes__when_course_is_in_courses__expect_notes_to_be_added(self):
        result = self.student.add_notes('OOP', 'error handling')
        self.assertEqual("Notes have been updated", result)
        self.assertEqual({'OOP': ['encapsulation', 'inheritance', 'polymorphism', 'abstraction', 'error handling'],
                                         'Algorithms': ['Graphs', 'DFS', 'BFS']}, self.student.courses)

    def test_add_notes__when_courses_is_not_in_courses__expect_error(self):
        with self.assertRaises(Exception) as ex:
            self.student.add_notes('Advanced', 'error handling')
        self.assertIsNotNone(ex)
        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_leave_course__when_course_is_in_courses__expect_to_be_removed(self):
        result = self.student.leave_course('Algorithms')
        self.assertEqual("Course has been removed", result)
        self.assertEqual({'OOP': ['encapsulation', 'inheritance', 'polymorphism', 'abstraction']}, self.student.courses)

    def test_leave_course__when_course_is_not_in_courses__expect_error(self):
        with self.assertRaises(Exception) as ex:
            self.student.leave_course('Basic')
        self.assertIsNotNone(ex)
        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))


if __name__ == '__main__':
    main()
