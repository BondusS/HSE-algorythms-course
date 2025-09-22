# На вход подается массив целых положительных чисел, разделенных пробелом.
# Нужно найти максимальную сумму элементов массива, которая делится на 2.
# Напишите тесты, которые проверяют функцию на разных случаях.

def max_even_sum(arr):
    length = len(arr)
    max_even = [0] * length
    max_odd = [0] * length

    # Базовый случай
    if arr[0] % 2 == 0:
        max_even[0] = arr[0]
    else:
        max_odd[0] = arr[0]

    # Основной цикл
    for index in range(1, length):
        if arr[index] % 2 == 0:  # Четный элемент
            max_even[index] = max(max_even[index - 1] + arr[index], max_even[index - 1])
            max_odd[index] = max(max_odd[index - 1] + arr[index], max_odd[index - 1])
        else:  # Нечетный элемент
            max_even[index] = max(max_odd[index - 1] + arr[index], max_even[index - 1])
            max_odd[index] = max(max_even[index - 1] + arr[index], max_odd[index - 1])

    return max_even[-1]


# Сложность алгоритма O(n) == линейная, n - кол-во чисел в последовательности


def input_from_keyboard():
    print('Введите элементы массива:')
    array = list(map(int, input().split()))
    print(max_even_sum(array))


# Старт программы
if __name__ == "__main__":
    input_from_keyboard()

    # Пример использования
    print('\nТесты:')
    print(max_even_sum([1, 2, 3, 4, 5]))  # Вывод: 14 | (2+3+4+5)
    print(max_even_sum([3, 7, 5, 9]))  # Вывод: 24 | (3+7+5+9)
    print(max_even_sum([19]))  # Вывод: | корнер кейс
