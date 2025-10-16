import re


def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    """Нормализует текст: приводит регистр, заменяет ё на е, убирает лишние пробелы."""
    if not isinstance(text, str):
        raise TypeError("Текст должен быть строкой")
    
    if not text:
        return ""
    
    # Замена ё на е
    if yo2e:
        text = text.replace('ё', 'е').replace('Ё', 'Е')
    
    # Приведение к нижнему регистру
    if casefold:
        text = text.casefold()
    
    # Замена управляющих символов на пробелы
    text = re.sub(r'[\t\r\n]+', ' ', text)
    
    # Убирание повторяющихся пробелов
    text = re.sub(r'\s+', ' ', text)
    
    return text.strip()


def tokenize(text: str) -> list[str]:
    """Разбивает текст на токены (слова)."""
    if not isinstance(text, str):
        raise TypeError("Текст должен быть строкой")
    
    if not text:
        return []
    
    # Регулярное выражение для поиска слов (буквы/цифры/_ и слова с дефисами)
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
    
    # Создаем список элементов для сортировки
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


