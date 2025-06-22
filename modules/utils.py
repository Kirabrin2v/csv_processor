def compare(value: float | str, operator: str, target: float | str) -> bool:
    try:
        value, target = float(value), float(target)
    except ValueError:
        pass

    if operator == "==":
        return value == target
    elif operator == ">":
        return value > target
    elif operator == "<":
        return value < target
    elif operator == ">=":
        return value >= target
    elif operator == "<=":
        return value <= target
    else:
        raise ValueError(f"Неизвестный оператор: {operator}")

def aggregate_column(data: list[dict[str, str]], column: str, op: str) -> float:
    numbers = [float(row[column]) for row in data]
    if op == "avg":
        return sum(numbers) / len(numbers)
    elif op == "min":
        return min(numbers)
    elif op == "max":
        return max(numbers)
    else:
        raise ValueError("Неподдерживаемая агрегирующая функция")

