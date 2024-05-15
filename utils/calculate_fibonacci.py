from datetime import datetime


def calculate_fibonacci(n) -> int:
    """Вычисление числа Фибоначчи"""
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return calculate_fibonacci(n - 1) + calculate_fibonacci(n - 2)


def calculate_fibonacci_for_today() -> int:
    """Вычисление числа Фибоначчи для текущего дня месяца +1"""
    today = datetime.now()
    n = today.day + 1
    return calculate_fibonacci(n)
