import textwrap
from functools import total_ordering

@total_ordering
class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lecture(self, lecturer, course, grade):
        if (
            isinstance(lecturer, Lecturer)
            and course in lecturer.courses_attached
            and course in self.courses_in_progress
            and 0 <= int(grade) <= 10
        ):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return "Ошибка"
        
    def _average_grade(self):
        all_grades = []
        if self.grades:
            for v in self.grades.values():
                all_grades.extend(v)
            return sum(all_grades) / len(all_grades)
        else:
            return "у студента еще нет оценок"
        
    def __str__(self):
        return textwrap.dedent(f"""\
        Имя: {self.name}
        Фамилия: {self.surname}
        Средняя оценка за домашние задания: {self._average_grade()}
        Курсы в процессе изучения: {', '.join(self.courses_in_progress)}
        Завершенные курсы: {', '.join(self.finished_courses)}\
        """)
    
    def __eq__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        if isinstance(self._average_grade(), str):
            return 'У студента слева еще нет оценок'
        elif isinstance(other._average_grade(), str):
            return 'У студента справа еще нет оценок'
        else:
            return self._average_grade() == other._average_grade()
    
    def __lt__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        if isinstance(self._average_grade(), str):
            return 'У студента слева еще нет оценок'
        elif isinstance(other._average_grade(), str):
            return 'У студента справа еще нет оценок'
        else:
            return self._average_grade() < other._average_grade()

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student, reviewer, course, grade):
        if (
            isinstance(student, Student)
            and isinstance(reviewer, Reviewer)
            and course in self.courses_attached
            and course in student.courses_in_progress
        ):
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return "Ошибка"

@total_ordering
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def _average_grade(self):
        all_grades = []
        if self.grades:
            for v in self.grades.values():
                all_grades.extend(v)
            return sum(all_grades) / len(all_grades)
        else:
            return "у лектора еще нет оценок"
        
    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        if isinstance(self._average_grade(), str):
            return 'У лектора слева еще нет оценок'
        elif isinstance(other._average_grade(), str):
            return 'У лектора справа еще нет оценок'
        else:
            return self._average_grade() == other._average_grade()
    
    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        if isinstance(self._average_grade(), str):
            return 'У лектора слева еще нет оценок'
        elif isinstance(other._average_grade(), str):
            return 'У лектора справа еще нет оценок'
        else:
            return self._average_grade() < other._average_grade()
        

    def __str__(self):
        return textwrap.dedent(f"""\
                               Имя: {self.name}
                               Фамилия: {self.surname}
                               Средняя оценка за лекции: {self._average_grade()}\
        """)


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def __str__(self):
        return textwrap.dedent(f"""\
                               Имя: {self.name}
                               Фамилия: {self.surname}\
        """)


lecturerd_1 = Lecturer("Иван", "Иванов")
lecturerd_2 = Lecturer("Александр", "Филатов")
reviewer = Reviewer("Пётр", "Петров")
student_1 = Student(surname="Алёхина", name="Ольга", gender="Ж")
student_2 = Student(surname="Сидорова", name="Елена", gender="Ж")
student_1.courses_in_progress += ["Python", "Java"]
student_1.finished_courses += ["Введение в программирование"]
student_2.courses_in_progress += ["Python", "Java"]
student_2.finished_courses += ["Введение в программирование"]
lecturerd_1.courses_attached += ["Python", "Java"]
lecturerd_2.courses_attached += ["Python", "Java"]
reviewer.courses_attached.append("Python")
reviewer.rate_hw(student=student_1, reviewer=reviewer, course="Python", grade=8)
reviewer.rate_hw(student=student_1, reviewer=reviewer, course="Python", grade=5)
reviewer.rate_hw(student=student_2, reviewer=reviewer, course="Python", grade=10)
reviewer.rate_hw(student=student_2, reviewer=reviewer, course="Python", grade=5)
student_1.rate_lecture(lecturerd_1, "Python", 7)
student_1.rate_lecture(lecturerd_1, "Python", 5)
student_1.rate_lecture(lecturerd_1, "Python", 10)
student_1.rate_lecture(lecturerd_1, "Java", 6)
student_1.rate_lecture(lecturerd_1, "Java", 4)
student_1.rate_lecture(lecturerd_2, "Python", 3)
student_1.rate_lecture(lecturerd_2, "Python", 2)
student_1.rate_lecture(lecturerd_2, "Python", 4)
student_1.rate_lecture(lecturerd_2, "Java", 5)
student_1.rate_lecture(lecturerd_2, "Java", 6)

print(reviewer)
print()
print(lecturerd_1)
print()
print(student_1)
print()
print(student_2)
print()
print(lecturerd_1 == lecturerd_2)
print(lecturerd_1 > lecturerd_2)
print()
print(student_1 == student_2)
print(student_1 > student_2)
print(student_1 < student_2)
print(student_1 >= student_2)


