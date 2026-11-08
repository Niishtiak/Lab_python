from models import Department, Discipline
from faculty_logic import Faculty
from exceptions import FacultyException

def setup_faculty_data() -> Faculty:
    faculty = Faculty("Факультет радиофизики и компьютерных технологий (ФРиКТ БГУ)")

    # Реальные кафедры ФРиКТ БГУ
    dept_is = Department("Кафедра интеллектуальных систем")
    dept_cs = Department("Кафедра информатики и компьютерных систем")
    dept_kb = Department("Кафедра кибербезопасности и информационных технологий")
    dept_rf = Department("Кафедра радиофизики и цифровых медиатехнологий")

    for d in [dept_is, dept_cs, dept_kb, dept_rf]:
        faculty.add_department(d)

    # Чистые дисциплины без лишних кодов
    d_math = Discipline("Математический анализ")
    d_discrete = Discipline("Дискретная математика")
    d_cpp = Discipline("Программирование на C++")
    d_py = Discipline("Программирование на Python")
    d_ai = Discipline("Многоагентные системы и ИИ")
    d_sec = Discipline("Криптографические методы защиты")
    d_optics = Discipline("Оптика")

    # Привязка дисциплин к специальностям
    specs = ["интеллектуальные системы", "прикладная информатика", "компьютерная безопасность", "радиофизика"]
    for spec in specs:
        dept_cs.add_discipline(spec, d_math)
        dept_cs.add_discipline(spec, d_cpp)

    # Профильные для Интеллектуальных систем
    dept_is.add_discipline("интеллектуальные системы", d_py)
    dept_is.add_discipline("интеллектуальные системы", d_ai)
    dept_is.add_discipline("интеллектуальные системы", d_discrete)

    # Профильные для КБ
    dept_kb.add_discipline("компьютерная безопасность", d_sec)

    # Профильные для Радиофизики
    dept_rf.add_discipline("радиофизика", d_optics)

    # Автоматически создаем пару студентов для теста
    # 1. Анастасия (Интеллектуальные системы)
    st1 = faculty.enroll_student("101", "Анастасия", "интеллектуальные системы")
    faculty.add_student_to_discipline("101", "Математический анализ")
    faculty.add_student_to_discipline("101", "Программирование на Python")
    faculty.add_student_to_discipline("101", "Многоагентные системы и ИИ")
    faculty.set_grade("101", "Математический анализ", 9)
    faculty.set_grade("101", "Программирование на Python", 10)

    # 2. Алексей (Компьютерная безопасность)
    st2 = faculty.enroll_student("102", "Алексей", "компьютерная безопасность")
    faculty.add_student_to_discipline("102", "Математический анализ")
    faculty.add_student_to_discipline("102", "Криптографические методы защиты")
    faculty.set_grade("102", "Математический анализ", 8)

    return faculty

def main():
    faculty = setup_faculty_data()

    print(f"=== {faculty.name} ===")
    
    while True:
        print("\n— ГЛАВНОЕ МЕНЮ —")
        print("1. Показать всех студентов")
        print("2. Зачислить нового студента")
        print("3. Выбрать студента по ID и управлять (курсы, оценки, перевод)")
        print("4. Отчислить студента")
        print("0. Выход")
        
        choice = input("Выберите действие: ").strip()

        if choice == "1":
            print("\n--- Список студентов ---")
            if not faculty.students:
                print("Студентов пока нет.")
            for sid, st in faculty.students.items():
                status = "Активен" if st.is_active else "Отчислен"
                print(f"[{sid}] {st.name} | Спец: {st.specialty} | Семестр: {st.semester} | Статус: {status}")
                courses = [f"{d_name} ({st.grades.get(d_name, 'нет оценки')})" for d_name in st.enrolled_disciplines]
                print(f"    Дисциплины: {'; '.join(courses) if courses else 'нет'}")

        elif choice == "2":
            s_id = input("Введите ID студента: ").strip()
            name = input("Введите ФИО студента: ").strip()
            spec = input("Введите специальность (интеллектуальные системы / прикладная информатика / компьютерная безопасность / радиофизика): ").strip().lower()
            try:
                faculty.enroll_student(s_id, name, spec)
                print(f"Студент {name} (ID: {s_id}) успешно зачислен!")
            except Exception as e:
                print(f"Ошибка: {e}")

        elif choice == "3":
            s_id = input("Введите ID студента: ").strip()
            try:
                student = faculty.get_student(s_id)
            except FacultyException as e:
                print(f"Ошибка: {e}")
                continue

            while True:
                print(f"\n— Студент: {student.name} [ID: {student.student_id}, Спец: {student.specialty}, Семестр: {student.semester}] —")
                print("1. Записать на дисциплину")
                print("2. Удалить дисциплину")
                print("3. Выставить оценку (1-10)")
                print("4. Перевести на следующий семестр")
                print("5. Сформировать ведомость в .txt файл")
                print("0. Назад в главное меню")

                sub_choice = input("Выберите действие: ").strip()

                try:
                    if sub_choice == "1":
                        disc_name = input("Введите название дисциплины: ").strip()
                        faculty.add_student_to_discipline(s_id, disc_name)
                        print(f"Студент успешно записан на курс '{disc_name}'!")

                    elif sub_choice == "2":
                        disc_name = input("Введите название дисциплины: ").strip()
                        faculty.remove_student_from_discipline(s_id, disc_name)
                        print(f"Дисциплина '{disc_name}' удалена у студента.")

                    elif sub_choice == "3":
                        disc_name = input("Введите название дисциплины: ").strip()
                        grade = int(input("Введите оценку (1-10): ").strip())
                        faculty.set_grade(s_id, disc_name, grade)
                        print(f"Оценка {grade} за курс '{disc_name}' успешно выставлена!")

                    elif sub_choice == "4":
                        faculty.promote_student(s_id)
                        print(f"Студент успешно переведён на {student.semester} семестр!")

                    elif sub_choice == "5":
                        filename = faculty.generate_student_report(s_id)
                        print(f"Ведомость сохранена в файл: {filename}")

                    elif sub_choice == "0":
                        break
                    else:
                        print("Некорректный ввод.")
                except FacultyException as e:
                    print(f"Ошибка операции: {e}")
                except ValueError:
                    print("Ошибка: Введите корректное числовое значение для оценки!")

        elif choice == "4":
            s_id = input("Введите ID студента для отчисления: ").strip()
            try:
                faculty.expell_student(s_id)
                print(f"Студент с ID {s_id} успешно отчислен.")
            except FacultyException as e:
                print(f"Ошибка: {e}")

        elif choice == "0":
            print("Завершение работы программы.")
            break
        else:
            print("Некорректный выбор.")

if __name__ == "__main__":
    main()