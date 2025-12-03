import json
from typing import List
from models import Student

def students_to_json(students: List[Student], path: str) -> None:
    """Сериализация с базовой проверкой"""
    if not students:
        print("Внимание: пустой список студентов")
        return
    
    data = [student.to_dict() for student in students]
    
    try:
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"Сохранено {len(students)} студентов в {path}")
    except Exception as e:
        print(f"Ошибка при сохранении: {e}")

def students_from_json(path: str) -> List[Student]:
    """Десериализация с обработкой ошибок"""
    try:
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"Файл не найден: {path}")
        return []
    except json.JSONDecodeError:
        print(f"Ошибка формата JSON в файле: {path}")
        return []
    
    if not isinstance(data, list):
        print(f"Ожидался список, получен {type(data).__name__}")
        return []
    
    students = []
    errors = []
    
    for i, item in enumerate(data):
        try:
            student = Student.from_dict(item)
            students.append(student)
        except (ValueError, KeyError, TypeError) as e:
            errors.append(f"Строка {i}: {e}")
    
    if errors:
        print("Найдены ошибки при загрузке:")
        for error in errors:
            print(f"  - {error}")
    
    return students

if __name__ == "__main__": # Проверка запущен ли скрипт напрямую
    # Пример использования
    students = [
        Student("Комаров Сергей", "2006-11-25", "SE-01", 4.6),
        Student("Каплан Алексей", "2007-10-14", "SE-02", 4.4),
        Student("Попова Александра", "2002-05-16", "SE-03", 3.8)
    ]
    
    # Сериализация
    students_to_json(students, "data/lab08/students_output.json")
    
    # Десериализация
    loaded_students = students_from_json("data/lab08/students_input.json")
    for student in loaded_students:
        print(student)