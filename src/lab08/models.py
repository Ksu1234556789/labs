from dataclasses import dataclass
from datetime import datetime, date
from typing import Dict, Any

@dataclass
class Student:
    fio: str
    birthdate: str
    group: str
    gpa: float

    def __post_init__(self):
        # Валидация даты
        try:
            datetime.strptime(self.birthdate, "%Y-%m-%d")
        except ValueError:
            raise ValueError(f"Неверный формат даты: {self.birthdate}. Используйте YYYY-MM-DD")
        
        # Валидация GPA
        if not (0 <= self.gpa <= 5):
            raise ValueError(f"GPA должен быть от 0 до 5, получено: {self.gpa}")
        
        # Валидация ФИО 
        if len(self.fio.strip().split()) < 2:
            raise ValueError(f"ФИО должно содержать минимум 2 слова: {self.fio}")

    def age(self) -> int:
        birth_date = datetime.strptime(self.birthdate, "%Y-%m-%d").date()
        today = date.today()
        age = today.year - birth_date.year
        
        if (today.month, today.day) < (birth_date.month, birth_date.day):
            age -= 1
            
        return age

    def to_dict(self) -> Dict[str, Any]:
        return {
            "fio": self.fio,
            "birthdate": self.birthdate,
            "group": self.group,
            "gpa": self.gpa
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Student':
        # Проверка обязательных полей
        required = ['fio', 'birthdate', 'group', 'gpa']
        for field in required:
            if field not in data:
                raise KeyError(f"Отсутствует поле: {field}")
        
        return cls(
            fio=str(data["fio"]),
            birthdate=str(data["birthdate"]),
            group=str(data["group"]),
            gpa=float(data["gpa"])
        )

    def __str__(self) -> str:
        return f"{self.fio}, {self.group}, GPA: {self.gpa:.2f}, Возраст: {self.age()}"
    

if __name__ == "__main__":
    try:
        student = Student(
            fio="Сидорова Анна Петровна", # Аргумент: ФИО
            birthdate="2005-06-28",
            group="SE-01",
            gpa=4.6
        )
        print(student)
        print(f"Словарь: {student.to_dict()}")
    except ValueError as e:
        print(f"Ошибка: {e}")