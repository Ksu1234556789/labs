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