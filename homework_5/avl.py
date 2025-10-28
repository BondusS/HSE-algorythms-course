# Реализовать класс AVL, который будет представлять собой avl-дерево.
# Поддержать следующие операции:
# * вставка
# * удаление
# * поиск


# Узел avl-дерева
class AVLNode:
    # Конструктор
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1  # Высота узла (листья имеют высоту 1)


# AVL-дерево
class AVLTree:
    # Конструктор
    def __init__(self):
        self.root = None

    # Возвращает высоту узла (0 для None)
    def get_height(self, node):
        return node.height if node else 0

    # Возвращает баланс узла (разность высот левого и правого поддеревьев)
    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    # Обновляет высоту узла на основе высот потомков
    def update_height(self, node):
        if node:
            node.height = max(self.get_height(node.left), self.get_height(node.right)) + 1

    # Правый поворот вокруг узла y
    def rotate_right(self, y):
        x = y.left
        T2 = x.right

        # Поворот
        x.right = y
        y.left = T2

        # Обновление высот
        self.update_height(y)
        self.update_height(x)

        return x  # Новый корень поддерева

    # Левый поворот вокруг узла x
    def rotate_left(self, x):
        y = x.right
        T2 = y.left

        # Поворот
        y.left = x
        x.right = T2

        # Обновление высот
        self.update_height(x)
        self.update_height(y)

        return y  # Новый корень поддерева

    # Вставка ключа в дерево
    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        # 1. Стандартная вставка BST
        if not node:
            return AVLNode(key)
        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)
        else:
            return node  # Дубликаты не вставляем

        # 2. Обновляем высоту текущего узла
        self.update_height(node)

        # 3. Получаем баланс
        balance = self.get_balance(node)

        # 4. Балансировка (4 случая)
        # Лево-левое
        if balance > 1 and key < node.left.key:
            return self.rotate_right(node)
        # Право-правое
        if balance < -1 and key > node.right.key:
            return self.rotate_left(node)
        # Лево-правое
        if balance > 1 and key > node.left.key:
            node.left = self.rotate_left(node.left)
            return self.rotate_right(node)
        # Право-левое
        if balance < -1 and key < node.right.key:
            node.right = self.rotate_right(node.right)
            return self.rotate_left(node)

        return node

    # Находит узел с минимальным ключом в поддереве
    def find_min(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    # Удаление ключа из дерева
    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        # 1. Стандартное удаление BST
        if not node:
            return node
        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            # Узел для удаления найден
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            # Узел имеет двух потомков: берём следующий по порядку
            temp = self.find_min(node.right)
            node.key = temp.key
            node.right = self._delete(node.right, temp.key)

        # 2. Обновляем высоту
        self.update_height(node)

        # 3. Получаем баланс
        balance = self.get_balance(node)

        # 4. Балансировка (4 случая)
        # Лево-левое
        if balance > 1 and self.get_balance(node.left) >= 0:
            return self.rotate_right(node)
        # Право-правое
        if balance < -1 and self.get_balance(node.right) <= 0:
            return self.rotate_left(node)
        # Лево-правое
        if balance > 1 and self.get_balance(node.left) < 0:
            node.left = self.rotate_left(node.left)
            return self.rotate_right(node)
        # Право-левое
        if balance < -1 and self.get_balance(node.right) > 0:
            node.right = self.rotate_right(node.right)
            return self.rotate_left(node)

        return node

    # Поиск ключа в дереве. Возвращает True, если найден
    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if not node:
            return False
        if key == node.key:
            return True
        elif key < node.key:
            return self._search(node.left, key)
        else:
            return self._search(node.right, key)

    # Возвращает список ключей в порядке in‑order
    def inorder(self):
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node, result):
        if node:
            self._inorder(node.left, result)
            result.append(node.key)
            self._inorder(node.right, result)


# Старт программы
if __name__ == "__main__":
    # Тесты

    tree = AVLTree()

    # Пустое дерево
    print(tree.inorder())  # []
    print(tree.search(1))  # False

    # Вставка одного элемента
    tree.insert(10)
    print(tree.inorder())  # [10]
    print(tree.search(10))  # True
    print(tree.search(5))  # False

    # Вставка нескольких элементов (без балансировки)
    tree.insert(5)
    tree.insert(15)
    print(tree.inorder())  # [5, 10, 15]
    print(tree.search(5) and tree.search(15))  # True

    # Вставка с балансировкой (лево-левое вращение)
    tree = AVLTree()
    tree.insert(3)
    tree.insert(2)
    tree.insert(1)  # Должно вызвать правый поворот
    print(tree.inorder())  # [1, 2, 3]

    # Вставка с балансировкой (право-правое вращение)
    tree = AVLTree()
    tree.insert(1)
    tree.insert(2)
    tree.insert(3)  # Должно вызвать левый поворот
    print(tree.inorder())  # [1, 2, 3]

    # Вставка с балансировкой (лево-правое вращение)
    tree = AVLTree()
    tree.insert(3)
    tree.insert(1)
    tree.insert(2)  # Должно вызвать лево-правое вращение
    print(tree.inorder())  # [1, 2, 3]

    # Вставка с балансировкой (право-левое вращение)
    tree = AVLTree()
    tree.insert(1)
    tree.insert(3)
    tree.insert(2)  # Должно вызвать право-левое вращение
    print(tree.inorder())  # [1, 2, 3]

    # Удаление листа
    tree = AVLTree()
    for key in [5, 3, 7, 2, 4, 6, 8]:
        tree.insert(key)
    tree.delete(2)  # Удаляем лист
    print(tree.inorder())  # [3, 4, 5, 6, 7, 8]
    print(tree.search(2))  # False

    # Удаление узла с одним потомком
    tree = AVLTree()
    for key in [5, 3, 7, 4, 6, 8]:
        tree.insert(key)
    tree.delete(3)  # У 3 есть только правый потомок (4)
    print(tree.inorder())  # [4, 5, 6, 7, 8]
    print(tree.search(3))  # False

    # Удаление узла с двумя потомками
    tree = AVLTree()
    for key in [5, 3, 7, 2, 4, 6, 8]:
        tree.insert(key)
    tree.delete(5)  # У 5 два потомка; заменится на 6
    print(tree.inorder())  # [2, 3, 4, 6, 7, 8]
    print(tree.search(5))  # False

    # Удаление корня (дерево из 1 элемента)
    tree = AVLTree()
    tree.insert(10)
    tree.delete(10)
    print(tree.inorder())  # []
    print(tree.search(10))  # False

    # Удаление с последующей балансировкой (лево-левое)
    tree = AVLTree()
    for key in [4, 2, 6, 1, 3, 5, 7, 0]:
        tree.insert(key)
    tree.delete(7)  # Должно спровоцировать балансировку
    print(abs(tree.get_balance(tree.root)) <= 1)  # True

    # Удаление с последующей балансировкой (право-правое)
    tree = AVLTree()
    for key in [3, 1, 5, 0, 2, 4, 6, 7]:
        tree.insert(key)
    tree.delete(0)  # Должно спровоцировать балансировку
    print(abs(tree.get_balance(tree.root)) <= 1)  # True

    # Повторная вставка существующего ключа
    tree = AVLTree()
    tree.insert(5)
    tree.insert(5)  # Дубликат — не должен изменить дерево
    print(tree.inorder())  # [5]

    # Поиск в пустом дереве
    tree = AVLTree()
    print(tree.search(1))  # False

    # Удаление несуществующего ключа
    tree = AVLTree()
    for key in [3, 1, 5]:
        tree.insert(key)
    tree.delete(4)  # Ключа нет — дерево не меняется
    print(tree.inorder())  # [1, 3, 5]
