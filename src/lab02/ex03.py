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

print(format_record(["Иванов Иван Иванович", "BIVT-25", 4.6]))