# Напишите программу, которая проверяет, является ли целое положительное число палиндромом.
# Сделайте это без использования строк.
# Напишите тесты, которые проверяют функцию на разных случаях.

def is_palindrome(number):
    # Обработка отрицательных чисел
    if number < 0:
        return False
    # Находим делитель для извлечения первой цифры
    divisor = 1
    while number // divisor >= 10:
        divisor *= 10
    # Проверяем цифры с обоих концов
    while number > 0:
        # Извлекаем первую и последнюю цифры
        first_digit = number // divisor
        last_digit = number % 10
        # Если цифры не совпадают, возвращаем False
        if first_digit != last_digit:
            return False
        # Удаляем первую и последнюю цифры
        number = (number % divisor) // 10
        # Уменьшаем делитель в 100 раз (убрали 2 цифры)
        divisor //= 100
    return True


# Сложность алгоритма O(n) == линейная, n - кол-во цифр в числе


def input_from_keyboard():
    print('Введите число:')
    chislo = int(input())
    print(is_palindrome(chislo))


# Старт программы
if __name__ == "__main__":
    input_from_keyboard()

    # Примеры использования
    print(is_palindrome(121))  # True
    print(is_palindrome(12321))  # True
    print(is_palindrome(123))  # False
    print(is_palindrome(10))  # False
    print(is_palindrome(1))  # True
