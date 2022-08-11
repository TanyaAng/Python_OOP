from unittest import TestCase, main
from project.student_report_card import StudentReportCard


class TestStudentReportCard(TestCase):
    STUDENT_NAME = 'Pesho'
    SCHOOL_YEAR = 5

    def setUp(self):
        self.student = StudentReportCard(self.STUDENT_NAME, self.SCHOOL_YEAR)

    def test_attr__when_its_valid(self):
        self.assertEqual(self.STUDENT_NAME, self.student.student_name)
        self.assertEqual(self.SCHOOL_YEAR, self.student.school_year)
        self.assertEqual({}, self.student.grades_by_subject)

    def test_attr_student_name__when_its_empty_string(self):
        with self.assertRaises(ValueError) as ex:
            StudentReportCard('', self.SCHOOL_YEAR)
        self.assertEqual("Student Name cannot be an empty string!", str(ex.exception))

    def test_attr_student_name__when_its_many_whitespaces(self):
        new_student = StudentReportCard('  ', self.SCHOOL_YEAR)
        self.assertEqual('  ', new_student.student_name)
        self.assertEqual(self.SCHOOL_YEAR, new_student.school_year)

    def test_attr_school_year__when_its_above_twelve(self):
        with self.assertRaises(ValueError) as ex:
            StudentReportCard('Gosho', 15)
        self.assertEqual("School Year must be between 1 and 12!", str(ex.exception))

    def test_attr_school_year__when_its_below_one(self):
        with self.assertRaises(ValueError) as ex:
            StudentReportCard('Gosho', 0)
        self.assertEqual("School Year must be between 1 and 12!", str(ex.exception))

    def test_attr_school_year__when_its_float_number(self):
        new_student = StudentReportCard('Stamat', 5.67)
        self.assertEqual(5.67, new_student.school_year)


    def test_set_atrr__when_both_are_invalid(self):
        with self.assertRaises(ValueError) as ex:
            StudentReportCard('', -5)
        self.assertEqual('Student Name cannot be an empty string!', str(ex.exception))

    def test_add_grade__when_it_is_successfully_added(self):
        self.student.add_grade('math', 4.00)
        self.student.add_grade('math', 5.00)
        self.student.add_grade('math', 6.00)
        self.assertEqual({'math': [4.00, 5.00, 6.00]}, self.student.grades_by_subject)

    def test_add_grade__return_value(self):
        result = self.student.add_grade('History', 6.00)
        self.assertEqual(None, result)

    def test_average_grade_by_subject(self):
        self.student.add_grade('math', 4.00)
        self.student.add_grade('math', 5.00)
        self.student.add_grade('math', 6.00)
        self.student.add_grade('geography', 3.00)
        self.assertEqual("math: 5.00\ngeography: 3.00", self.student.average_grade_by_subject())

    def test_average_grade_by_subject__when_dont_have_subjects_yet(self):
        self.assertEqual('', self.student.average_grade_by_subject())

    def test_average_grade_for_all_subject__when_have_subjects(self):
        self.student.add_grade('math', 4.00)
        self.student.add_grade('math', 5.00)
        self.student.add_grade('math', 6.00)
        self.student.add_grade('geography', 3.00)
        self.assertEqual("Average Grade: 4.50", self.student.average_grade_for_all_subjects())

    def test_average_grade_for_all_subjects__when_dont_have_subject_yet(self):
        with self.assertRaises(ZeroDivisionError) as ex:
            self.student.average_grade_for_all_subjects()
        self.assertEqual('division by zero', str(ex.exception))

    def test_repr__when_student_has_grades(self):
        self.student.add_grade('math', 4.00)
        self.student.add_grade('math', 5.00)
        self.student.add_grade('math', 6.00)
        self.student.add_grade('geography', 3.00)
        expected_result = f"Name: {self.STUDENT_NAME}\n" \
                          f"Year: {self.SCHOOL_YEAR}\n" \
                          f"----------\n" \
                          f"math: 5.00\ngeography: 3.00\n" \
                          f"----------\n" \
                          f"Average Grade: 4.50"
        self.assertEqual(expected_result, repr(self.student))

    def test_repr__when_student_has_no_grades(self):
        with self.assertRaises(ZeroDivisionError) as ex:
            repr(self.student)
        self.assertEqual('division by zero', str(ex.exception))


if __name__ == '__main__':
    main()
