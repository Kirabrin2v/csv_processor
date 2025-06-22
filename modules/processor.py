import csv
from .utils import compare, aggregate_column

def process_csv(filepath, where, aggregate):
    with open(filepath, newline='', encoding='utf-8') as f:
        reader = list(csv.DictReader(f))
    
    if where:
        col, op, val = parse_filter(where)
        if len(reader) == 0 or col not in reader[0]:
            raise ValueError(f"Поля с названием '{col}' не существует")

        reader = [row for row in reader if compare(row[col], op, val)]

    if aggregate:
        col, func = aggregate.split("=")
        result = aggregate_column(reader, col, func)
        return {"headers": [func], "data": [[result]]}

    return {"headers": reader[0].keys() if reader else [], "data": [row.values() for row in reader]}

def parse_filter(condition):
    ops = [(">=", ">="), ("<=", "<="), (">", ">"), ("<", "<"), ("=", "==")]
    for symbol, op in ops:
        if symbol in condition:
            col, val = condition.split(symbol)
            return col.strip(), op, val.strip()
    raise ValueError("Некорректное условие фильтра. Пример использования: column>value")

