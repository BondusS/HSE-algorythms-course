# Реализовать рекурсивные версии mergesort и quicksort.
# Реализовать декоратор, который будет замерять время выполнения функции.
# Придумать тесты, на которых время выполнения этих методов будет прилично отличаться.

import time
from functools import wraps
import random


# Декоратор измерения времени выполнения функции
def time_measure(func):
    @wraps(func)  # Сохраняет метаданные оригинальной функции
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        print(f"Функция {args[0].__name__} выполнена за {end_time - start_time:.6f} секунд")
        return result
    return wrapper


# Применение декоратора измерения времени
@time_measure
def test_sort(sort_func, data):
    return sort_func(data.copy())


# Сортировка слиянием
def merge_sort(arr):

    # Слияние
    def merge(left, right):
        result = []
        i, j = 0, 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result

    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)


# Быстрая сортировка
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


# Старт программы
if __name__ == "__main__":
    # Семплы для тестов

    # Случай 1: Почти отсортированный массив
    sorted_data = list(range(100000))
    random.shuffle(sorted_data[:100])  # Немного нарушаем порядок

    # Случай 2: Обратно отсортированный массив
    reverse_data = list(range(100000, 0, -1))

    # Случай 3: Массив с большим количеством одинаковых элементов
    duplicates_data = [random.randint(1, 100) for _ in range(100000)]

    # Случай 4: Случайный массив
    random_data = [random.randint(1, 100000) for _ in range(100000)]

    # Тесты
    print("Тестирование на почти отсортированном массиве:")
    test_sort(merge_sort, sorted_data)
    test_sort(quick_sort, sorted_data)

    print("\nТестирование на обратно отсортированном массиве:")
    test_sort(merge_sort, reverse_data)
    test_sort(quick_sort, reverse_data)

    print("\nТестирование на массиве с дубликатами:")
    test_sort(merge_sort, duplicates_data)
    test_sort(quick_sort, duplicates_data)

    print("\nТестирование на случайном массиве:")
    test_sort(merge_sort, random_data)
    test_sort(quick_sort, random_data)
