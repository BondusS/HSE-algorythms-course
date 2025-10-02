# Даны 2 последовательности pushed и popped, содержащие уникальные целые числа.
# popped является перестановкой pushed, то есть, все элементы совпадают, но может отличаться порядок.
# Программа должна вернуть True, если эти последовательности могут получиться
# в результате некоторой последовательности операций push и pop на пустом стеке.

from stack_vs_queue import Stack


def validate_stack_sequences(pushed, popped):
    stack = Stack()
    pop_index = 0
    for x in pushed:
        stack.push(x)  # кладем элемент в стек
        # Пока можем делать pop — выполняем его
        while not stack.is_empty() and stack.peek() == popped[pop_index]:
            stack.pop()
            pop_index += 1
    return pop_index == len(popped)


# Сложность алгоритма O(n) == линейная, n - кол-во чисел в последовательностях


# Старт программы
if __name__ == "__main__":
    # Примеры использования
    pushed1 = [1, 2, 3, 4, 5]
    popped1 = [4, 5, 3, 2, 1]
    print(validate_stack_sequences(pushed1, popped1))  # Выведет: True
    pushed2 = [1, 2, 3, 4, 5]
    popped2 = [1, 3, 5, 4, 2]
    print(validate_stack_sequences(pushed2, popped2))  # Выведет: True
    pushed3 = [1, 2, 3]
    popped3 = [3, 1, 2]
    print(validate_stack_sequences(pushed3, popped3))  # Выведет: False
