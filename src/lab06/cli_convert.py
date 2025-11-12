import argparse
from pathlib import Path
try:
    from lab05.json_csv import *
except ImportError:
    # Альтернативный импорт для тестирования
    import os
    import sys
    sys.path.append(os.path.dirname(os.path.dirname(__file__)))
    from lab05.json_csv import *
try:
    from lab05.csv_xlsx import *
except ImportError:
    # Альтернативный импорт для тестирования
    import os
    import sys
    sys.path.append(os.path.dirname(os.path.dirname(__file__)))
    from lab05.csv_xlsx import *


def main():
    parser = argparse.ArgumentParser(description="Конвертер JSON в CSV, CSV в JSON, CSV в XLSX")
    sub = parser.add_subparsers(dest="cmd")

    # json → csv
    json2csv_parser = sub.add_parser("json2csv", help="Конвертировать JSON в CSV")
    json2csv_parser.add_argument("--in", dest="input", required=True, help="Путь к входному JSON")
    json2csv_parser.add_argument("--out", dest="output", required=True, help="Путь к выходному CSV")

    # csv → json
    csv2json_parser = sub.add_parser("csv2json", help="Конвертировать CSV в JSON")
    csv2json_parser.add_argument("--in", dest="input", required=True, help="Путь к входному CSV")
    csv2json_parser.add_argument("--out", dest="output", required=True, help="Путь к выходному JSON")

    # csv → xlsx
    csv2xlsx_parser = sub.add_parser("csv2xlsx", help="Конвертировать CSV в XLSX")
    csv2xlsx_parser.add_argument("--in", dest="input", required=True, help="Путь к входному CSV")
    csv2xlsx_parser.add_argument("--out", dest="output", required=True, help="Путь к выходному XLSX")

    args = parser.parse_args()

    if not args.cmd:
        parser.print_help()
        return

    input_path = Path(args.input)
    if not input_path.exists():
        parser.error(f"Входной файл '{args.input}' не найден")

    # Создаем выходную директорию если не существует
    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    try:
        if args.cmd == "json2csv":
            json_to_csv(args.input, args.output)
            print(f"Успешно конвертировано: {args.input} -> {args.output}")
            
        elif args.cmd == "csv2json":
            csv_to_json(args.input, args.output)
            print(f"Успешно конвертировано: {args.input} -> {args.output}")
            
        elif args.cmd == "csv2xlsx":
            csv_to_xlsx(args.input, args.output)
            print(f"Успешно конвертировано: {args.input} -> {args.output}")
            
    except Exception as e:
        parser.error(f"Ошибка конвертации: {e}")


if __name__ == "__main__":
    main()