import csv
from pathlib import Path
from typing import Iterable, Sequence

def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    """Читает файл и возвращает текст."""
    """
        Пользователь может выбрать другую кодировку, например: encoding="cp1251"
        для чтения файлов созданных в Windows на русском языке.
    """
    p = Path(path)

    if not p.exists():
        raise FileNotFoundError(f"Файл не найден: {path}")
    
    try:
        return p.read_text(encoding=encoding)
    except UnicodeDecodeError:
        raise


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

