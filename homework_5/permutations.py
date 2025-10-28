# На вход дан массив. Необходимо вернуть все возможные перестановки.
# В реализации предусмотреть визуализацию стека вызовов, в идеале использовать декоратор из первой задачи.


# Улучшенная версия визуализации рекурсии с читаемым представлением арументов
def tracer_upd(func):
    recursion_level = 0

    def wrapper(*args, **kwargs):
        nonlocal recursion_level
        indent = "  " * recursion_level

        # Читаемое представление аргументов
        args_repr = [repr(arg) for arg in args]
        kwargs_repr = [f"{k}={repr(v)}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)

        print(f"{indent}-> {func.__name__}({signature})")
        recursion_level += 1
        result = func(*args, **kwargs)
        recursion_level -= 1
        print(f"{indent}<- {result}")
        return result

    return wrapper


# Функция построения всех возможных перестановок массива, с декоратором, демонстрирующим рекурию
@tracer_upd
def permutations(nums):
    # Тривиальный случай: пустой список или один элемент
    if len(nums) <= 1:
        return [nums[:]]
    # Остальные случаи
    result = []
    for i in range(len(nums)):
        current = nums[i]  # текущий элемент
        remaining = nums[:i] + nums[i + 1:]  # оставшиеся элементы
        # Генерируем перестановки для оставшихся элементов
        for perm in permutations(remaining):
            # Добавляем текущий элемент в начало каждой перестановки
            result.append([current] + perm)
    return result


# Старт программы
if __name__ == "__main__":
    # Тесты
    test_cases = [[1, 2, 3], [0, 1], [1], [], ['a', 'b', 'c'], [1, 1, 2]]
    for case in test_cases:
        permutations(case)
        print('\n')
