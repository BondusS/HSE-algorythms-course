# Реализовать итеративные версии mergesort и quicksort.

import time
from functools import wraps
import random


# Сортировка слиянием (итеративная версия)
def iterative_merge_sort(arr):

    # Вспомогательная функция для слияния двух подмассивов
    def merge(arr, temp, left_start, right_end):
        # Определяем границы подмассивов
        left_end = (right_end + left_start) // 2
        right_start = left_end + 1
        size = right_end - left_start + 1
        i = left_start  # указатель на левый подмассив
        j = right_start  # указатель на правый подмассив
        k = left_start  # указатель на результирующий массив
        # Слияние двух подмассивов
        while i <= left_end and j <= right_end:
            if arr[i] <= arr[j]:
                temp[k] = arr[i]
                i += 1
            else:
                temp[k] = arr[j]
                j += 1
            k += 1
        # Копируем оставшиеся элементы левого подмассива
        while i <= left_end:
            temp[k] = arr[i]
            i += 1
            k += 1
        # Копируем оставшиеся элементы правого подмассива
        while j <= right_end:
            temp[k] = arr[j]
            j += 1
            k += 1
        # Копируем результат обратно в исходный массив
        for i in range(size):
            arr[left_start + i] = temp[left_start + i]

    n = len(arr)
    temp = [0] * n  # вспомогательный массив для слияния
    current_size = 1  # начальный размер подмассивов

    # Основной цикл сортировки
    while current_size < n:
        for left_start in range(0, n, 2 * current_size):
            mid = min(left_start + current_size - 1, n - 1)
            right_end = min(left_start + 2 * current_size - 1, n - 1)
            merge(arr, temp, left_start, right_end)
        current_size *= 2  # удваиваем размер подмассивов
    return arr


# Быстрая сортировка (итеративная версия)
def iterative_quick_sort(arr):

    # Вспомогательная функция для разбиения массива
    def partition(arr, low, high):
        pivot = arr[high]  # выбираем опорный элемент
        i = low - 1  # указатель на последний элемент меньше pivot
        # Проходим по массиву и переставляем элементы
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        # Ставим опорный элемент на его место
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1  # возвращаем индекс опорного элемента

    stack = [(0, len(arr) - 1)]  # стек для хранения границ подмассивов

    # Основной цикл сортировки
    while stack:
        low, high = stack.pop()  # извлекаем границы текущего подмассива
        if low < high:
            pivot_index = partition(arr, low, high)  # разбиваем массив
            # Добавляем в стек подмассивы для дальнейшей обработки
            if pivot_index - 1 > low:
                stack.append((low, pivot_index - 1))
            if pivot_index + 1 < high:
                stack.append((pivot_index + 1, high))
    return arr


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


# Старт программы
if __name__ == "__main__":
    # Семплы для тестов

    # Случай 1: Почти отсортированный массив
    sorted_data = list(range(10000))
    random.shuffle(sorted_data[:100])  # Немного нарушаем порядок

    # Случай 2: Обратно отсортированный массив
    reverse_data = list(range(10000, 0, -1))

    # Случай 3: Массив с большим количеством одинаковых элементов
    duplicates_data = [random.randint(1, 100) for _ in range(10000)]

    # Случай 4: Случайный массив
    random_data = [random.randint(1, 10000) for _ in range(10000)]

    # Тесты
    print("Тестирование на почти отсортированном массиве:")
    test_sort(iterative_merge_sort, sorted_data)
    test_sort(iterative_quick_sort, sorted_data)

    print("\nТестирование на обратно отсортированном массиве:")
    test_sort(iterative_merge_sort, reverse_data)
    test_sort(iterative_quick_sort, reverse_data)

    print("\nТестирование на массиве с дубликатами:")
    test_sort(iterative_merge_sort, duplicates_data)
    test_sort(iterative_quick_sort, duplicates_data)

    print("\nТестирование на случайном массиве:")
    test_sort(iterative_merge_sort, random_data)
    test_sort(iterative_quick_sort, random_data)
