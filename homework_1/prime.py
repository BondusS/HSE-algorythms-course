# На вход подается целое число N
# Нужно найти количество простых чисел < N.
# Напишите тесты, которые проверяют функцию на разных случаях.

def count_primes(number):
    # Обработка крайних случаев
    if number <= 2:
        return 0

    is_prime = [True] * number
    is_prime[0] = is_prime[1] = False  # 0 и 1 не простые

    for i_index in range(2, number):
        if is_prime[i_index]:
            # Отмечаем все кратные i как составные
            for j_index in range(i_index * 2, number, i_index):
                is_prime[j_index] = False

    return sum(is_prime)


def input_from_keyboard():
    print('Введите число:')
    chislo = int(input())
    print(count_primes(chislo))


# Старт программы
if __name__ == "__main__":
    input_from_keyboard()

    # Пример использования
    print('\nТесты:')
    print(count_primes(20))  # Вывод: 8 | (2, 3, 5, 7, 11, 13, 17, 19)
    print(count_primes(5))  # Вывод: 2 | (2, 3)
    print(count_primes(2))  # Вывод: 0 | корнер кейс
