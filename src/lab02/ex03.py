def format_record(rec: tuple[str, str, float]) -> str:
    fio, group, gpa = rec
    
    fio_parts = [part.strip() for part in fio.split() if part.strip()]
    
    if len(fio_parts) < 2:
        raise ValueError("ФИО должно содержать фамилию и имя")
    
    surname = fio_parts[0][0].upper() + fio_parts[0][1:].lower()
    initials = []
    
    for i in range(1, min(3, len(fio_parts))):
        if fio_parts[i]: 
            initials.append(f"{fio_parts[i][0].upper()}.")
    
    form_fio = f"{surname} {''.join(initials)}"
    
    form_group = group.strip()
    
    form_gpa = f"{gpa:.2f}"
    
    return f"{form_fio}, гр. {form_group}, GPA {form_gpa}"

print(format_record(["Иванов Иван Иванович", "BIVT-25", 4.6]))
print(format_record(["Петров Пётр", "IKBO-12", 5.0]))
print(format_record(["Петров Пётр Петрович", "IKBO-12", 5.0]))
print(format_record(["  сидорова  анна   сергеевна ", "ABB-01", 3.999]))
#print(format_record(["Иванов", "BIVT-25", 4.6]))