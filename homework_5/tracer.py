# Реализовать декоратор, который показывает стек вызовов рекурсивных функций
# На каждом шаге должен быть виден:
# * вход в рекурсию (вызов функции),
# * отступ, соответствующий глубине стека,
# * возврат из рекурсии с результатом


# Визуализация рекурсии
def tracer(func):
    recursion_level = 0  # текущий уровень вложенности рекурсии

    # Рекурсивный цикл вызова функции
    def wrapper(*args, **kwargs):
        nonlocal recursion_level  # использование внешней переменной уровня
        indent = "  " * recursion_level  # отступ
        print(f"{indent}-> {func.__name__}({', '.join(map(str, args))})")  # информация о входе в функцию
        recursion_level += 1
        result = func(*args, **kwargs)
        recursion_level -= 1
        print(f"{indent}<- {result}")  # информация о возврате из функции
        return result

    return wrapper


# Рекурсивная функция с декоратором для теста
@tracer
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


# Старт программы
if __name__ == "__main__":
    # Тестируем декоратор
    factorial(3)


# Вывод программы:
#
# -> factorial(3)
#   -> factorial(2)
#     -> factorial(1)
#       -> factorial(0)
#       <- 1
#     <- 1
#   <- 2
# <- 6
