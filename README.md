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
### №1 
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
```
### №2
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

```
### №3
```
def format_record(rec: tuple[str, str, float]) -> str:
    fio, group, gpa = rec
    
    fio_parts = [part.strip() for part in fio.split() if part.strip()]
    
    if len(fio_parts) < 2:
        raise ValueError("ФИО должно содержать фамилию и имя")
    
    surname = fio_parts[0]
    initials = []
    
    for i in range(1, min(3, len(fio_parts))):
        if fio_parts[i]: 
            initials.append(f"{fio_parts[i][0].upper()}.")
    
    form_fio = f"{surname} {''.join(initials)}"
    
    form_group = group.strip()
    
    form_gpa = f"{gpa:.2f}"
    
    return f"{form_fio}, гр. {form_group}, GPA {form_gpa}"
```