from models import Student, Department, Discipline
from exceptions import (
    StudentNotFoundException,
    CourseNotAvailableException,
    StudentNotEnrolledException,
    InvalidGradeException,
    FacultyException
)

class Faculty:
    def __init__(self, name: str):
        self.name = name
        self.students = {}      # { student_id: Student }
        self.departments = []   # список объектов Department

    def add_department(self, department: Department):
        self.departments.append(department)

    def enroll_student(self, student_id: str, name: str, specialty: str) -> Student:
        if student_id in self.students:
            raise FacultyException(f"Студент с ID '{student_id}' уже существует.")
        student = Student(student_id, name, specialty)
        self.students[student_id] = student
        return student

    def expell_student(self, student_id: str):
        student = self.get_student(student_id)
        student.is_active = False

    def get_student(self, student_id: str) -> Student:
        if student_id not in self.students or not self.students[student_id].is_active:
            raise StudentNotFoundException(f"Студент с ID '{student_id}' не найден или отчислен.")
        return self.students[student_id]

    def add_student_to_discipline(self, student_id: str, discipline_name: str):
        student = self.get_student(student_id)
        
        teaching_dept = None
        target_discipline = None

        for dept in self.departments:
            if dept.can_teach(student.specialty, discipline_name):
                teaching_dept = dept
                target_discipline = dept.get_discipline(student.specialty, discipline_name)
                break

        if not teaching_dept:
            raise CourseNotAvailableException(
                f"Ни одна кафедра не читает дисциплину '{discipline_name}' для специальности '{student.specialty}'."
            )

        student.enrolled_disciplines[target_discipline.name] = {
            "discipline": target_discipline,
            "department": teaching_dept
        }

    def remove_student_from_discipline(self, student_id: str, discipline_name: str):
        student = self.get_student(student_id)
        target_key = next((k for k in student.enrolled_disciplines if k.lower() == discipline_name.lower()), None)
        
        if not target_key:
            raise StudentNotEnrolledException(f"Студент не записан на дисциплину '{discipline_name}'.")
        
        del student.enrolled_disciplines[target_key]
        if target_key in student.grades:
            del student.grades[target_key]

    def set_grade(self, student_id: str, discipline_name: str, grade: int):
        student = self.get_student(student_id)
        target_key = next((k for k in student.enrolled_disciplines if k.lower() == discipline_name.lower()), None)
        
        if not target_key:
            raise StudentNotEnrolledException(f"Нельзя поставить оценку: студент не записан на курс '{discipline_name}'.")
        
        if not isinstance(grade, int) or not (1 <= grade <= 10):
            raise InvalidGradeException("Оценка должна быть целым числом от 1 до 10.")
            
        student.grades[target_key] = grade

    def promote_student(self, student_id: str):
        student = self.get_student(student_id)
        
        if not student.enrolled_disciplines:
            raise FacultyException("У студента нет записанных дисциплин для перевода.")
            
        for disc_name in student.enrolled_disciplines:
            if disc_name not in student.grades:
                raise FacultyException(f"Не выставлена оценка по дисциплине '{disc_name}'.")
            if student.grades[disc_name] < 4:
                raise FacultyException(f"Низкая оценка ({student.grades[disc_name]}) по дисциплине '{disc_name}'. Перевод невозможен.")
                
        student.semester += 1
        student.enrolled_disciplines.clear()
        student.grades.clear()

    def generate_student_report(self, student_id: str, filename: str = None) -> str:
        student = self.get_student(student_id)
        if not filename:
            filename = f"report_student_{student.student_id}.txt"

        lines = [
            "=== ВЕДОМОСТЬ УСПЕВАЕМОСТИ СТУДЕНТА ===",
            f"ID: {student.student_id}",
            f"ФИО: {student.name}",
            f"Специальность: {student.specialty}",
            f"Семестр: {student.semester}",
            "-" * 50,
            "Дисциплины:"
        ]

        for disc_name, data in student.enrolled_disciplines.items():
            dept_name = data["department"].name
            grade = student.grades.get(disc_name, "Нет оценки")
            lines.append(f"• {disc_name} | Кафедра: {dept_name} | Оценка: {grade}")

        lines.append("-" * 50)
        lines.append(f"Средний балл (GPA): {student.get_average_grade():.2f}\n")

        with open(filename, "w", encoding="utf-8") as f:
            f.write("\n".join(lines))
        
        return filename