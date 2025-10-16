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
