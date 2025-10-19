# Реализовать все обходы дерева:
# pre-order
# post-order
# in-order
# reverse pre-order
# reverse post-order
# reverse in-order
#
# Класс BST реализуем самостоятельно
# В классе BST необходимо поддержать вставку для удобства тестирования


# Узел дерева
class BSTNode:
    # Конструктор
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


# Дерево
class BST:
    # Конструктор
    def __init__(self):
        self.root = None

    # Вставка узла (первый или вызов вставки для непервого узла)
    def insert(self, key):
        if self.root is None:
            self.root = BSTNode(key)
        else:
            self._insert_recursive(self.root, key)

    # Вставка узла (не первого)
    def _insert_recursive(self, node, key):
        if key < node.key:
            if node.left is None:
                node.left = BSTNode(key)
            else:
                self._insert_recursive(node.left, key)
        else:
            if node.right is None:
                node.right = BSTNode(key)
            else:
                self._insert_recursive(node.right, key)

    # Обходы дерева
    def pre_order(self):
        return self._pre_order_recursive(self.root)

    def _pre_order_recursive(self, node):
        if node is None:
            return []
        return [node.key] + self._pre_order_recursive(node.left) + self._pre_order_recursive(node.right)

    def post_order(self):
        return self._post_order_recursive(self.root)

    def _post_order_recursive(self, node):
        if node is None:
            return []
        return self._post_order_recursive(node.left) + self._post_order_recursive(node.right) + [node.key]

    def in_order(self):
        return self._in_order_recursive(self.root)

    def _in_order_recursive(self, node):
        if node is None:
            return []
        return self._in_order_recursive(node.left) + [node.key] + self._in_order_recursive(node.right)

    def reverse_pre_order(self):
        return self._reverse_pre_order_recursive(self.root)

    def _reverse_pre_order_recursive(self, node):
        if node is None:
            return []
        return [node.key] + self._reverse_pre_order_recursive(node.right) + self._reverse_pre_order_recursive(node.left)

    def reverse_post_order(self):
        return self._reverse_post_order_recursive(self.root)

    def _reverse_post_order_recursive(self, node):
        if node is None:
            return []
        return self._reverse_post_order_recursive(node.right) + self._reverse_post_order_recursive(node.left) + [node.key]

    def reverse_in_order(self):
        return self._reverse_in_order_recursive(self.root)

    def _reverse_in_order_recursive(self, node):
        if node is None:
            return []
        return self._reverse_in_order_recursive(node.right) + [node.key] + self._reverse_in_order_recursive(node.left)


# Старт программы
if __name__ == "__main__":
    # Примеры использования

    # Инициализация дерева
    bst = BST()
    keys = [50, 30, 20, 40, 70, 60, 80]

    # Вставка элементов
    for key in keys:
        bst.insert(key)

    # Провки обходов
    print(bst.pre_order())  # [50, 30, 20, 40, 70, 60, 80]
    print(bst.post_order())  # [20, 40, 30, 60, 80, 70, 50]
    print(bst.in_order())  # [20, 30, 40, 50, 60, 70, 80]
    print(bst.reverse_pre_order())  # [50, 70, 80, 60, 30, 40, 20]
    print(bst.reverse_post_order())  # [80, 60, 70, 40, 20, 30, 50]
    print(bst.reverse_in_order())  # [80, 70, 60, 50, 40, 30, 20]
