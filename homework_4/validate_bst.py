# На вход приходит root бинарного дерева.
# Необходимо проверить, является ли это дерево бинарным деревом поиска.
#
# Тесты, в рамках которых необходимо рассмотреть как можно больше краевых кейсов.

# Узел дерева
class TreeNode:
    # Конструктор
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Проверка дерева на bst
def is_valid_bst(root):
    # Внутренняя функция для рекурсивных вызовов
    def validate(node, low=float('-inf'), high=float('inf')):
        # Базовый случай: пустое дерево - валидное BST
        if not node:
            return True
        # Текущее значение должно быть в пределах диапазона
        if node.val <= low or node.val >= high:
            return False
        # Рекурсивно проверяем левое и правое поддеревья
        return (validate(node.left, low, node.val) and
                validate(node.right, node.val, high))
    return validate(root)


# Старт программы
if __name__ == "__main__":
    # Примеры использования

    # Пустое дерево
    print(is_valid_bst(None))  # True

    # Один узел
    print(is_valid_bst(TreeNode(5)))  # True

    # Простая валидная структура
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    print(is_valid_bst(root))  # True

    # Невалидная структура (правый узел меньше корня)
    root = TreeNode(2)
    root.left = TreeNode(3)
    root.right = TreeNode(1)
    print(is_valid_bst(root))  # False

    # Сложный случай с несколькими уровнями
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(7)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(8)
    print(is_valid_bst(root))  # True

    # Крайний случай с дубликатами
    root = TreeNode(5)
    root.left = TreeNode(5)
    print(is_valid_bst(root))  # False

    # Крайний случай с большими числами
    root = TreeNode(2 ** 31 - 1)
    root.left = TreeNode(2 ** 31 - 2)
    print(is_valid_bst(root))  # True

    # Невалидная структура с нарушением в поддереве
    root = TreeNode(5)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root.right.left = TreeNode(3)
    root.right.right = TreeNode(6)
    print(is_valid_bst(root))  # False
