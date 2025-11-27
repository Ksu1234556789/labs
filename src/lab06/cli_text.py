import argparse
from pathlib import Path

try:
    from lib.text import normalize, tokenize, count_freq, top_n
except ImportError:
    # Альтернативный импорт для тестирования
    import os
    import sys

    sys.path.append(os.path.dirname(os.path.dirname(__file__)))
    from lib.text import normalize, tokenize, count_freq, top_n


def main():
    parser = argparse.ArgumentParser(description="CLI‑утилиты")
    subparsers = parser.add_subparsers(dest="command")

    # подкоманда cat
    cat_parser = subparsers.add_parser("cat", help="Вывести содержимое файла")
    cat_parser.add_argument("--input", required=True, help="Путь к файлу для вывода")
    cat_parser.add_argument("-n", action="store_true", help="Нумеровать строки")

    # подкоманда stats
    stats_parser = subparsers.add_parser("stats", help="Частоты слов")
    stats_parser.add_argument("--input", required=True, help="Путь к текстовому файлу")
    stats_parser.add_argument("--top", type=int, default=5, help="Количество топ-слов")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return

    file_path = Path(args.input)
    if not file_path.exists():
        parser.error(f"Файл '{args.input}' не найден")

    if args.command == "cat":
        try:
            with file_path.open("r", encoding="utf-8") as f:
                for i, line in enumerate(f, start=1):
                    line = line.rstrip("\n")
                    if args.n:
                        print(f"{i:6}  {line}")
                    else:
                        print(line)
        except Exception as e:
            parser.error(f"Ошибка при чтении файла: {e}")

    elif args.command == "stats":
        try:
            with file_path.open("r", encoding="utf-8") as f:
                text = f.read()

            normalized = normalize(text)
            words = tokenize(normalized)
            freq = count_freq(words)
            top_words = top_n(freq, args.top)

            if not top_words:
                print("Слова не найдены в файле")
                return

            print(f"Топ-{args.top} самых частых слов:")
            print("Слово\t\tЧастота")
            print("-" * 20)
            for word, count in top_words:
                print(f"{word:<15} {count}")

        except Exception as e:
            parser.error(f"Ошибка при анализе текста: {e}")


if __name__ == "__main__":
    main()

# python -m src.lab06.cli_text cat --input data/samples/people.csv -n
# python -m src.lab06.cli_text stats --input data/samples/people.txt
