# Даны два отсортированных односвязных списка list1 и list2
# Необходимо объединить их в один новый отсортированный список.
# Новый список должен быть составлен слиянием узлов двух исходных списков.
# Вернуть необходимо голову объединенного списка.
# реализовать два способа решения поставленной задачи: с использованием фиктивного элемента и без него

class ListNode:
    # Конструктор
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Решение с использованием фиктивного элемента
def merge_two_lists_wf(list1, list2):
    dummy = ListNode(-1)  # фиктивный узел
    current = dummy
    # Цикл обхода списков
    while list1 and list2:
        if list1.val <= list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next
    # Присоединяем остаток одного из списков
    if list1:
        current.next = list1
    else:
        current.next = list2
    return dummy.next  # пропускаем фиктивный узел


# Решение без использования фиктивного элемента
def merge_two_lists_nf(list1, list2):
    # Определяем голову результата
    if not list1:
        return list2
    if not list2:
        return list1
    if list1.val <= list2.val:
        head = list1
        list1 = list1.next
    else:
        head = list2
        list2 = list2.next
    current = head
    # Цикл обхода списков
    while list1 and list2:
        if list1.val <= list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next
    # Присоединяем остаток одного из списков
    if list1:
        current.next = list1
    else:
        current.next = list2
    return head


# Преобразование массива в связный список
def list_to_linked_list(lst):
    if not lst:
        return None
    head = ListNode(lst[0])
    current = head
    for value in lst[1:]:
        current.next = ListNode(value)
        current = current.next
    return head


# Преобразование связного списка в массив
def linked_list_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result


# Использование методов с массивами
def using(list_1, list_2, merge_func):
    l_list_1 = list_to_linked_list(list_1)
    l_list_2 = list_to_linked_list(list_2)
    answer = merge_func(l_list_1, l_list_2)
    return linked_list_to_list(answer)


# Старт программы
if __name__ == "__main__":
    # Примеры использования
    list1_1 = [1, 2, 3]
    list2_1 = [1, 3, 5]
    print(f' По методу с фиктивным элементов:   {using(list1_1, list2_1, merge_two_lists_wf)}\n',
          f'По методу без фиктивного элемента: {using(list1_1, list2_1, merge_two_lists_nf)}\n')
    list1_2 = [1, 3, 5, 7, 9]
    list2_2 = [2, 4, 6, 8]
    print(f' По методу с фиктивным элементов:   {using(list1_2, list2_2, merge_two_lists_wf)}\n',
          f'По методу без фиктивного элемента: {using(list1_2, list2_2, merge_two_lists_nf)}\n')
