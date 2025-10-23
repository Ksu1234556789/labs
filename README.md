# Лабораторная работа №1

### №1 - Вывод прграммы: имя и возраст через год
```
name = (input('Имя: '))
age = int(input('Возраст: '))
print('Привет, ', name, '! Через год тебе будет ', age+1, '.', sep='')
```

![№1 - Вывод первого задания](img/lab01/img-01.png)
### №2 - Вывод прграммы: сумма и среднее число
```
a = float(input('a: ').replace(',', '.'))
b = float(input('b: ').replace(',', '.'))
sum = round(a+b, 2)
avg = round(sum/2, 2)
print('sum=',sum,'; avg=', avg, sep = '')
```

![№2 - Вывод второго задания](img/lab01/img-02.png)
### №3 - Вывод прграммы: база после скидки, НДС, итог к оплате
```
price = float(input('Цена(₽): ').replace(',','.'))
discount = float(input('Скидка(%): ').replace(',','.'))
vat = float(input('НДС(%): ').replace(',','.'))
base = price * (1 - discount/100)
vat_amount = base * (vat/100)
total = base + vat_amount
print(f'База после скидки: {base:.2f} ₽')
print(f'НДС: {vat_amount:.2f} ₽')
print(f'Итого к оплате: {total:.2f} ₽')
```

![№3 - Вывод третьего задания](img/lab01/img-03.png)
### №4 - Вывод прграммы: время
```
m = int(input('Минуты:'))
hours = m // 60
minutes = m % 60
print(f"{hours}:{minutes:02d}")
```

![№4 - Вывод четвертого задания](img/lab01/img-04.png)
### №5 -  Вывод прграммы: инициалы и цена
```
name = input('ФИО:').strip()
parts = name.split()
initials = ''.join(part[0].upper() for part in parts) + '.'
length =len(' '.join(parts))
print('Инициалы:', initials)
print('Длина (символов):', length)
```

![№5 - Вывод пятого задания](img/lab01/img-05.png)

# Лабораторная работа №2
### №1 Работа со списками
```
def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    if not nums:
        raise ValueError("Список пуст")
    min_n = nums[0]
    max_n = nums[0]
    for num in nums:
        if num < min_n:
            min_n = num
        if num > max_n:
            max_n = num
    return (min_n, max_n)

def unique_sorted(nums: list[float | int]) -> list[float | int]:
    return sorted(set(nums))



def flatten(mat: list[list | tuple]) -> list:
    result = []
    for item in mat:
        if not isinstance(item, (list, tuple)):
            raise TypeError("Строка не строка строк матрицы")
        
        result.extend(item)
    
    return result


print(min_max([3, -1, 5, 5, 0]))
print(min_max([42]))
print(min_max([-5, -2, -9]))
#print(min_max([ ]))
print(min_max([1.5, 2, 2.0, -3.1]))

print(unique_sorted([3, 1, 2, 1, 3]))
print(unique_sorted([]))
print(unique_sorted([-1, -1, 0, 2, 2]))
print(unique_sorted([1.0, 1, 2.5, 2.5, 0]))

print(flatten([[1, 2], [3, 4]]))
print(flatten(([1, 2], (3, 4, 5))))
print(flatten([[1], [], [2, 3]]))
#print(flatten([[1, 2], 'ab']))

```
![(error 1)](img/lab02/img-2-01.png)
![error 2)](img/lab02/img-2-02.png)
![Вывод первого задания](img/lab02/img-2-03.png)
### №2 Функции (для прямоугольных матриц)
```
def check_rec(mat: list[list]) -> tuple[int, int]:
    if not mat:
        return 0, 0
    
    rows = len(mat)
    cols = len(mat[0])
    
    for i in range(rows):
        if len(mat[i]) != cols:
            raise ValueError("Матрица должна быть прямоугольной")
    
    return rows, cols

def transpose(mat: list[list[float | int]]) -> list[list]:
    rows, cols = check_rec(mat)
    if rows == 0:
        return []
    
    result = []
    for j in range(cols):
        new_row = []
        for i in range(rows):
            new_row.append(mat[i][j])
        result.append(new_row)
    
    return result

def row_sums(mat: list[list[float | int]]) -> list[float]:
    rows, cols = check_rec(mat)
    
    if rows == 0:
        return []
    
    sums = []
    for i in range(rows):
        row_sum = 0
        for j in range(cols):
            row_sum += mat[i][j]
        sums.append(row_sum)
    
    return sums

def col_sums(mat: list[list[float | int]]) -> list[float]:

    rows, cols = check_rec(mat)
    
    if cols == 0:
        return []
    
    sums = []
    for j in range(cols):
        col_sum = 0
        for i in range(rows):
            col_sum += mat[i][j]
        sums.append(col_sum)
    
    return sums

print(transpose([[1, 2, 3]]))
print(transpose([[1], [2], [3]]))
print(transpose([[1, 2], [3, 4]]))
print(transpose([ ]))
#print(transpose([[1, 2], [3]]))

print(row_sums([[1, 2, 3], [4, 5, 6]]))
print(row_sums([[-1, 1], [10, -10]]))
print(row_sums([[0, 0], [0, 0]]))
#print(row_sums([[1, 2], [3]]))

print(col_sums([[1, 2, 3], [4, 5, 6]]))
print(col_sums([[-1, 1], [10, -10]]))
print(col_sums([[0, 0], [0, 0]]))
#print(col_sums([[1, 2], [3]]))

```
![(error 1)](img/lab02/img-2-04.png)
![Вывод второго задания](img/lab02/img-2-05.png)

### №3 Форматирование записей
```
def format_record(rec: tuple[str, str, float]) -> str:
    
    if not isinstance(rec, tuple):
        raise TypeError("Входные данные должны быть кортежем")
    
    if len(rec) != 3:
        raise ValueError("Кортеж должен содержать 3 элемента: (ФИО, группа, GPA)")
    
    fio, group, gpa = rec
    
    if not isinstance(fio, str):
        raise TypeError("ФИО должно быть строкой")
    
    if not isinstance(group, str):
        raise TypeError("Название группы должно быть строкой")
    
    if not isinstance(gpa, (int, float)):
        raise TypeError("GPA должно быть числом")
    
    if not fio.strip():
        raise ValueError("ФИО не может быть пустым")
    
    if not group.strip():
        raise ValueError("Название группы не может быть пустым")
    
    if gpa < 0 or gpa > 5.0:  
        raise ValueError("GPA должно быть в диапазоне от 0 до 5.0")
    

    fio_parts = [part.strip() for part in fio.split() if part.strip()]
    

    if len(fio_parts) < 2:
        raise ValueError("ФИО должно содержать фамилию и хотя бы одно имя")
    

    capital_parts = []
    for part in fio_parts:
        if not part:  
            raise ValueError("Части ФИО не могут быть пустыми")
        capital_parts.append(part[0].upper() + part[1:].lower())
    

    initials = []
    for name in capital_parts[1:]:  
        if len(name) < 1:
            raise ValueError("Имена не могут быть пустыми")
        initials.append(f"{name[0].upper()}.")
    

    formatted_fio = f"{capital_parts[0]} {' '.join(initials)}"
    

    formatted_gpa = f"{gpa:.2f}"
    

    return f"{formatted_fio}, гр. {group}, GPA {formatted_gpa}"



print(format_record(("Иванов Иван Иванович", "BIVT-25", 4.6)))
print(format_record(("  сидорова  анна   сергеевна ", "ABB-01", 3.999)))
print(format_record(["Петров Пётр", "IKBO-12", 5.0]))
print(format_record(["Петров Пётр Петрович", "IKBO-12", 5.0]))

```
![(error 1)](img/lab02/img-2-006.png)
![Вывод третьего задания](img/lab02/img-2-007.png)

# Лабораторная работа №3
### №1 - text.py
###### Нормализация текста, разбиение на слова, подсчитывание частоты и распределение по алфавиту и убыванию частоты


```
import re


def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    """Нормализует текст: приводит регистр, заменяет ё на е, убирает лишние пробелы."""
    if not isinstance(text, str):
        raise TypeError("Текст должен быть строкой")
    
    if not text:
        return ""
    
    
    if yo2e:
        text = text.replace('ё', 'е').replace('Ё', 'Е')
    
    
    if casefold:
        text = text.casefold()
    
    
    text = re.sub(r'[\t\r\n]+', ' ', text)
    
    
    text = re.sub(r'\s+', ' ', text)
    
    return text.strip()


def tokenize(text: str) -> list[str]:
    """Разбивает текст на токены (слова)."""
    if not isinstance(text, str):
        raise TypeError("Текст должен быть строкой")
    
    if not text:
        return []
    
    
    pattern = r'\b\w+(?:-\w+)*\b'
    tokens = re.findall(pattern, text)
    
    return tokens


def count_freq(tokens: list[str]) -> dict[str, int]:
    """Подсчитывает частоту встречаемости токенов."""
    if not isinstance(tokens, list):
        raise TypeError("Токены должны быть списком")
    
    freq_dict = {}
    for token in tokens:
        freq_dict[token] = freq_dict.get(token, 0) + 1
    
    return freq_dict


def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    """Возвращает топ-N самых частых слов."""
    if not isinstance(freq, dict):
        raise TypeError("Частоты должны быть словарем")
    if not isinstance(n, int) or n < 0:
        raise ValueError("n должно быть неотрицательным целым числом")
    
    if not freq:
        return []
    
    
    items = list(freq.items())
    
    # Сортировка по убыванию частоты, при равенстве - по алфавиту
    items.sort(key=lambda x: (-x[1], x[0]))
    
    return items[:n]

if __name__ == "__main__":

    print(normalize('ПрИвЕт\nМИр\t'))
    print(normalize('ёжик, Ёлка'))
    print(normalize('Hello\r\nWorld'))
    print(normalize('  двойные   пробелы  '))

    print(tokenize('привет мир'))
    print(tokenize('hello,world!!!'))
    print(tokenize('по-настоящему круто'))
    print(tokenize('2025 год'))
    print(tokenize('emoji 😀 не слово'))

    tokence1 = count_freq(["a", "b", "a", "c", "b", "a"])
    print(tokence1)
    print(top_n(tokence1, 2))

    tokence2 = count_freq(["bb","aa","bb","aa","cc"])
    print(tokence2)
    print(top_n(tokence2, 2))


```
![№1 - Вывод второго задания](img/lab03/img-3-02.png)

### №2 - text_stats.py

###### Находит кол-во слов и кол-во уникальных слов, а также топ-5 слов. Ввод происходит через терминал таким способом: echo "Привет, мир! Привет!!!" | python3 src/lab03/text_stats.py

```

import sys

# Импортируем наши функции из той же папки
try:
    from lib.text import normalize, tokenize, count_freq, top_n
except ImportError:
    # Альтернативный импорт для тестирования
    import os
    import sys
    sys.path.append(os.path.dirname(os.path.dirname(__file__)))
    from lib.text import normalize, tokenize, count_freq, top_n


def main():
    """Основная функция скрипта статистики текста."""
    # Читаем весь ввод из stdin
    text = sys.stdin.read()
    
    if not text.strip():
        print("Входной текст пуст")
        return
    
    try:
        # Обрабатываем текст
        normalized_text = normalize(text)
        tokens = tokenize(normalized_text)
        freq_dict = count_freq(tokens)
        top_words = top_n(freq_dict, 5)
        
        # Выводим результаты
        print(f"Всего слов: {len(tokens)}")
        print(f"Уникальных слов: {len(freq_dict)}")
        print("Топ-5:")
        
        for word, count in top_words:
            print(f"{word}:{count}")
            
    except Exception as e:
        print(f"Ошибка обработки текста: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()


```
![№2 - Вывод второго задания](img/lab03/img-3-03.png)
![№2 - Вывод второго задания](img/lab03/img-3-04.png)

# Лабораторная работа №4
### №1 - io_txt_csv.py
###### read_text - читает текстовый файл и возвращает его содержимое как строку. Чтение в формате UTF-8 по умолчанию. Для работы с файлами в разных кодировках можно указать: "utf-8" (по умолчанию), "cp1251" или "windows-1251" (русская кодировка Windows), "koi8-r" (русская кодировка для UNIX-систем), "iso-8859-5" (другая русская кодировка), "cp866" (русская кодировка DOS). 
###### write_csv - записывает данные в CSV.
###### ensure_parent_dir - создает родительские директории, если они не существуют.

```
import csv
from pathlib import Path
from typing import Iterable, Sequence

def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    """Читает файл и возвращает текст."""
    p = Path(path)
    return p.read_text(encoding=encoding)

def write_csv(rows: Iterable[Sequence], path: str | Path,
              header: tuple[str, ...] | None = None) -> None:
    p = Path(path)
    rows = list(rows)
    """Записывает данные в CSV файл."""
    # Проверка одинаковой длины строк
    if rows:
        first_len = len(rows[0])
        for i, row in enumerate(rows):
            if len(row) != first_len:
                raise ValueError(f"Строка {i} имеет длину {len(row)}, ожидается {first_len}")

    ensure_parent_dir(path)

    with p.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if header is not None:
            w.writerow(header)
        for r in rows:
            w.writerow(r)

def ensure_parent_dir(path: str | Path) -> None:
    """Создает родительские директории, если их нет."""
    Path(path).parent.mkdir(parents=True, exist_ok=True)

if __name__ == "__main__":
    txt = read_text("data/input.txt")  # должен вернуть строку
    print("Прочитано:", txt)
    write_csv([("word","count"),("test",3)], "data/check.csv") 
    print("CSV создан")


```
###### Вывод первого задания
![№1 - Вывод первого задания](img/lab04/img-4-01.png)


### №2 - text_report.py
###### Скрипт анализирует текстовый файл, подсчитывает частоты слов и генерирует CSV отчет.

```
import sys
from collections import Counter

try:
    from lab04.io_txt_csv import read_text, write_csv, ensure_parent_dir
except ImportError:
    #Альтернативный импорт для тестирования
    import os
    sys.path.append(os.path.dirname(os.path.dirname(__file__)))
    from lab04.io_txt_csv import read_text, write_csv, ensure_parent_dir
from lib.text import normalize, tokenize, count_freq, top_n

def frequencies_from_text(text: str) -> dict[str, int]:
    """
    Генерация частот из текста .
    """
    tokens = tokenize(normalize(text))
    return Counter(tokens)

def sorted_word_counts(freq: dict[str, int]) -> list[tuple[str, int]]:
    """
    Сортировка частот по шаблону: (-частота, слово).
    """
    return sorted(freq.items(), key=lambda kv: (-kv[1], kv[0]))

def generate_report():
    """
    Генерирует отчет по частотам слов.
    """
    input_file = "data/input.txt"
    output_file = "data/report.csv"
    
    try:
        # 1 Чтение текста 
        text = read_text(input_file)
        
        # 2 Подсчет частот через шаблонную функцию
        freq = frequencies_from_text(text)
        
        # 3 Сортировка по шаблону
        sorted_words = sorted_word_counts(freq)
        
        # 4 Сохранение отчета
        ensure_parent_dir(output_file)
        write_csv(sorted_words, output_file, header=("word", "count"))
        
        # 5 Вывод статистики в консоль
        tokens = tokenize(normalize(text))
        print(f"Всего слов: {len(tokens)}")
        print(f"Уникальных слов: {len(freq)}")
        print("Топ-5:")
        
        for word, count in top_n(freq, 5):
            print(f"{word}: {count}")
            
    except FileNotFoundError:
        print(f"Ошибка: Файл {input_file} не найден")
        sys.exit(1)
    except UnicodeDecodeError:
        print(f"Ошибка: Неверная кодировка файла {input_file}")
        print("Попробуйте указать кодировку: read_text(path, encoding='ваша кодировка')")
        sys.exit(1)
    except Exception as e:
        print(f"Ошибка: {e}")
        sys.exit(1)

if __name__ == "__main__":
    generate_report()


```
###### Вывод при input.txt - Привет, мир! Привет!!!
![№2 - Вывод второго задания](img/lab04/img-4-02.png)
###### report.csv при input.txt - Привет, мир! Привет!!!
![№2 - Вывод второго задания](img/lab04/img-4-03.png)
###### report.csv при пустом input.txt 
![№2 - Вывод второго задания](img/lab04/img-4-04.png)
###### Вывод при input.txt в cp1251 с текстом Привет
![№2 - Вывод второго задания](img/lab04/img-4-05.png)