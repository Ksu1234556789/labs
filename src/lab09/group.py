import csv
from pathlib import Path
try:
    from lab08.models import Student
except ImportError:
    # Альтернативный импорт для тестирования
    import os
    import sys
    sys.path.append(os.path.dirname(os.path.dirname(__file__)))
    from lab08.models import Student

class Group:
    def __init__(self, storage_path: str):
        self.path = Path(storage_path)
        self._ensure_storage_exists()

    def _ensure_storage_exists(self):
        """Создать файл с заголовком, если его ещё нет"""
        if not self.path.exists():
            self.path.parent.mkdir(parents=True, exist_ok=True)
            with self.path.open("w", encoding="utf-8", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(["fio", "birthdate", "group", "gpa"])

    def _read_all(self):
        """Прочитать все строки из CSV"""
        students = []
        if not self.path.exists():
            return students
            
        with self.path.open("r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                try:
                    student = Student(
                        fio=row["fio"],
                        birthdate=row["birthdate"],
                        group=row["group"],
                        gpa=float(row["gpa"])
                    )
                    students.append(student)
                except (ValueError, KeyError):
                    continue  # Пропускаем некорректные строки
        return students

    def list(self):
        """Вернуть всех студентов в виде списка Student"""
        return self._read_all()

    def add(self, student: Student):
        """Добавить нового студента в CSV"""
        with self.path.open("a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow([student.fio, student.birthdate, student.group, student.gpa])

    def find(self, substr: str):
        """Найти студентов по подстроке в fio"""
        substr = substr.lower()
        students = self._read_all()
        return [s for s in students if substr in s.fio.lower()]

    def remove(self, fio: str):
        """Удалить запись"""
        students = self._read_all()
        students = [s for s in students if s.fio != fio]
        
        with self.path.open("w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["fio", "birthdate", "group", "gpa"])
            for s in students:
                writer.writerow([s.fio, s.birthdate, s.group, s.gpa])

    def update(self, fio: str, **fields):
        """Обновить поля студента"""
        students = self._read_all()
        
        for student in students:
            if student.fio == fio:
                for key, value in fields.items():
                    if hasattr(student, key):
                        setattr(student, key, value)
                break
        
        with self.path.open("w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["fio", "birthdate", "group", "gpa"])
            for st in students:
                writer.writerow([st.fio, st.birthdate, st.group, st.gpa])


# Пример использования класса Group
if __name__ == "__main__":

    group = Group("/Users/ksu_k/Desktop/labs/data/lab09/students.csv")
    
    group.add(Student('Кошелапова Ксения Валентиновна', '2006-02-09', 'БИВТ-25-6', 4.8))
    group.add(Student('Иванов Иван Иванович', '2005-05-15', 'БИВТ-24-9', 4.6))

    # Выводим всех студентов
    print("Все студенты:")
    for s in group.list():
        print(f"  - {s.fio}, {s.group}, GPA: {s.gpa}")

    group.add(Student("Петров Василий Александрович", "2000-08-02", "БИВТ-20-9", 4.5))

    print("\nВсе студенты после добавления:")
    for s in group.list():
        print(f"  - {s.fio}, {s.group}, GPA: {s.gpa}")
    
    # Ищем студентов
    print("\nПоиск 'Иванов':")
    found = group.find('Иванов')
    for s in found:
        print(f"  - {s.fio}")
    
    # Обновляем данные
    group.update('Иванов Иван Иванович', gpa=4.7, group='БИВТ-21-2')

    print("\nПосле обновления:")
    for s in group.list():
        print(f"  - {s.fio}, {s.group}, GPA: {s.gpa}")

    group.remove("Петров Василий Александрович")

    print("\nПосле удаления:")
    for s in group.list():
        print(f"  - {s.fio}, {s.group}, GPA: {s.gpa}")

