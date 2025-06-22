import argparse
from modules.processor import process_csv
from tabulate import tabulate

def parse_args():
    parser = argparse.ArgumentParser(description="CSV Processor")
    parser.add_argument("file", help="Путь к CSV-файлу")
    parser.add_argument("--where", help="Условие фильтрации")
    parser.add_argument("--aggregate", help="Функция и столбец агрегации. Доступные функции: avg|min|max")
    return parser.parse_args()

def main():
    args = parse_args()
    try:
        result = process_csv(args.file, args.where, args.aggregate)
        print(tabulate(result["data"], headers=result["headers"], tablefmt="grid"))
    except Exception as e:
        print(f"Ошибка: {e}")

if __name__ == "__main__":
    main()

