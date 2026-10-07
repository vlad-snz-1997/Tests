from task_1 import Student, Mentor, Lecturer, Reviewer
import unittest
#python3 -m unittest

class TestStudent(unittest.TestCase):
    def setUp(self):
        self.student = Student("Алёхина", "Ольга", "Ж")

    def test_student_initialization(self):
        self.assertEqual(self.student.name, "Алёхина")
        self.assertEqual(self.student.surname, "Ольга")
        self.assertEqual(self.student.gender, "Ж")
        self.assertEqual(self.student.finished_courses, [])
        self.assertEqual(self.student.courses_in_progress, [])
        self.assertEqual(self.student.grades, {})

    def test_courses_in_progress_update(self):
        self.student.courses_in_progress += ["Python", "Java"]
        self.assertIn("Python", self.student.courses_in_progress)
        self.assertIn("Java", self.student.courses_in_progress)


class TestMentor(unittest.TestCase):
    def setUp(self):
        self.mentor = Mentor("Иван", "Иванов")

    def test_mentor_initialization(self):
        self.assertEqual(self.mentor.name, "Иван")
        self.assertEqual(self.mentor.surname, "Иванов")
        self.assertEqual(self.mentor.courses_attached, [])

    def test_rate_hw_success(self):
        student = Student("Алёхина", "Ольга", "Ж")
        student.courses_in_progress = ["Python"]
        self.mentor.courses_attached = ["Python"]

        result = self.mentor.rate_hw(student, "Python", 5)
        # При успешном выставлении оценки метод ничего не возвращает (None)
        self.assertIsNone(result)
        self.assertIn("Python", student.grades)
        self.assertEqual(student.grades["Python"], [5])

    def test_rate_hw_course_not_in_mentor_courses(self):
        student = Student("Алёхина", "Ольга", "Ж")
        student.courses_in_progress = ["Python"]
        self.mentor.courses_attached = []  # курса нет у ментора

        result = self.mentor.rate_hw(student, "Python", 5)
        self.assertEqual(result, "Ошибка")
        self.assertEqual(student.grades, {})  # оценка не добавлена

    def test_rate_hw_course_not_in_student_courses(self):
        student = Student("Алёхина", "Ольга", "Ж")
        student.courses_in_progress = []  # студент не проходит этот курс
        self.mentor.courses_attached = ["Python"]

        result = self.mentor.rate_hw(student, "Python", 5)
        self.assertEqual(result, "Ошибка")
        self.assertEqual(student.grades, {})

    #@unittest.expectedFailure
    def test_rate_hw_invalid_student(self):
        # Передаём не Student
        fake_student = {"name": "Fake"}
        self.mentor.courses_attached = ["Python"]

        result = self.mentor.rate_hw(fake_student, "Python", 5)
        self.assertEqual(result, "Ошибка")

    def test_rate_hw_multiple_grades(self):
        student = Student("Алёхина", "Ольга", "Ж")
        student.courses_in_progress = ["Python"]
        self.mentor.courses_attached = ["Python"]

        self.mentor.rate_hw(student, "Python", 4)
        self.mentor.rate_hw(student, "Python", 5)

        self.assertIn("Python", student.grades)
        self.assertEqual(student.grades["Python"], [4, 5])


class TestLecturerInheritance(unittest.TestCase):
    def test_lecturer_is_instance_of_mentor(self):
        lecturer = Lecturer("Иван", "Иванов")
        self.assertIsInstance(lecturer, Mentor)
        self.assertIsInstance(lecturer, Lecturer)

    def test_lecturer_initialization(self):
        lecturer = Lecturer("Иван", "Иванов")
        self.assertEqual(lecturer.name, "Иван")
        self.assertEqual(lecturer.surname, "Иванов")
        self.assertEqual(lecturer.courses_attached, [])


class TestReviewerInheritance(unittest.TestCase):
    def test_reviewer_is_instance_of_mentor(self):
        reviewer = Reviewer("Пётр", "Петров")
        self.assertIsInstance(reviewer, Mentor)
        self.assertIsInstance(reviewer, Reviewer)

    def test_reviewer_initialization(self):
        reviewer = Reviewer("Пётр", "Петров")
        self.assertEqual(reviewer.name, "Пётр")
        self.assertEqual(reviewer.surname, "Петров")
        self.assertEqual(reviewer.courses_attached, [])


if __name__ == "__main__":
    unittest.main()
