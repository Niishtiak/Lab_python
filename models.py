class Discipline:
    def __init__(self, name: str):
        self.name = name

    def __repr__(self):
        return self.name


class Department:
    def __init__(self, name: str):
        self.name = name
        # Словарь связей: { specialty_name: [Discipline, ...] }
        self.specialty_courses = {}

    def add_discipline(self, specialty: str, discipline: Discipline):
        spec_lower = specialty.lower()
        if spec_lower not in self.specialty_courses:
            self.specialty_courses[spec_lower] = []
        if discipline not in self.specialty_courses[spec_lower]:
            self.specialty_courses[spec_lower].append(discipline)

    def can_teach(self, specialty: str, discipline_name: str) -> bool:
        spec_lower = specialty.lower()
        if spec_lower in self.specialty_courses:
            return any(d.name.lower() == discipline_name.lower() for d in self.specialty_courses[spec_lower])
        return False

    def get_discipline(self, specialty: str, discipline_name: str):
        spec_lower = specialty.lower()
        if spec_lower in self.specialty_courses:
            for d in self.specialty_courses[spec_lower]:
                if d.name.lower() == discipline_name.lower():
                    return d
        return None


class Student:
    def __init__(self, student_id: str, name: str, specialty: str, semester: int = 1):
        self.student_id = student_id
        self.name = name
        self.specialty = specialty
        self.semester = semester
        self.is_active = True
        # Записанные дисциплины: { discipline_name: {"discipline": Discipline, "department": Department} }
        self.enrolled_disciplines = {}
        # Оценки: { discipline_name: grade }
        self.grades = {}

    def is_enrolled_in(self, discipline_name: str) -> bool:
        return any(k.lower() == discipline_name.lower() for k in self.enrolled_disciplines)

    def get_average_grade(self) -> float:
        if not self.grades:
            return 0.0
        return sum(self.grades.values()) / len(self.grades)