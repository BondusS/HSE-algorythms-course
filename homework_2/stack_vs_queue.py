# Реализовать стек и очередь на основе связных списков. Без использования сторонних библиотек.


# Реализация базового элемента - узел (Node)
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Реализация стека
class Stack:
    # Конструктор
    def __init__(self):
        self.top = None  # указатель на верхний элемент

    # Проверка на пустоту
    def is_empty(self):
        return self.top is None

    # Реализация метода Push (Положить элемент)
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top  # новый узел ссылается на предыдущий верхний
        self.top = new_node       # обновляем указатель на верхний элемент

    # Реализация метода Pop (Достать элемент)
    def pop(self):
        if self.is_empty():
            raise IndexError("Попытка достать элемент из пустого стека")
        popped_node = self.top
        self.top = self.top.next  # сдвигаем указатель на следующий элемент
        return popped_node.data

    # Реализация метода Peek (Посмотреть элемент)
    def peek(self):
        if self.is_empty():
            raise IndexError("Попытка посмотреть элемент из пустого стека")
        return self.top.data


# Реализация очереди
class Queue:
    # Конструктор
    def __init__(self):
        self.first = None  # указатель на первый элемент
        self.last = None   # указатель на последний элемент

    # Проверка на пустоту
    def is_empty(self):
        return self.first is None

    # Реализация метода Push (Положить элемент)
    def push(self, data):
        new_node = Node(data)
        if self.last is None:  # если очередь пуста
            self.first = self.last = new_node
            return
        self.last.next = new_node
        self.last = new_node

    # Реализация метода Pop (Достать элемент)
    def pop(self):
        if self.is_empty():
            raise IndexError("Попытка достать элемент из пустой очереди")
        dequeued_node = self.first
        self.first = self.first.next
        if self.first is None:  # если очередь стала пустой
            self.last = None
        return dequeued_node.data

    # Реализация метода Peek (Посмотреть элемент)
    def peek(self):
        if self.is_empty():
            raise IndexError("Попытка посмотреть элемент из пустой очереди")
        return self.first.data


# Старт программы
if __name__ == "__main__":
    # Пример работы со стеком
    stack = Stack()      # stack: {}
    stack.push(1)        # stack: {1}
    stack.push(2)        # stack: {2, 1}
    stack.push(3)        # stack: {3, 2, 1}
    print(stack.pop())   # 3 | stack: {2, 1}
    print(stack.peek())  # 2 | stack: {2, 1}

    # Пример работы с очередью
    queue = Queue()      # queue: {}
    queue.push(1)        # queue: {1}
    queue.push(2)        # queue: {2, 1}
    queue.push(3)        # queue: {3, 2, 1}
    print(queue.pop())   # 1 | stack: {3, 2}
    print(queue.peek())  # 2 | stack: {3, 2}
