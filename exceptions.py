class FacultyException(Exception):
    """Базовое исключение для факультета"""
    pass

class StudentNotFoundException(FacultyException):
    """Студент не найден или отчислен"""
    pass

class CourseNotAvailableException(FacultyException):
    """Кафедра не читает данный курс для специальности студента"""
    pass

class StudentNotEnrolledException(FacultyException):
    """Студент не записан на данную дисциплину"""
    pass

class InvalidGradeException(FacultyException):
    """Некорректное значение оценки"""
    pass