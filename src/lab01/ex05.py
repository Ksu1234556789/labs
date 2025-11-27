name = input("ФИО:").strip()
parts = name.split()
initials = "".join(part[0].upper() for part in parts) + "."
length = len(" ".join(parts))
print("Инициалы:", initials)
print("Длина (символов):", length)
