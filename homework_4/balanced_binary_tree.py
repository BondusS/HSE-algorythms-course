# Дано бинарное дерево. Определить, является ли оно сбалансированным по высоте.
#
# Сбалансированное по высоте бинарное дерево — это бинарное дерево,
# в котором глубина двух поддеревьев каждого узла никогда не отличается более чем на единицу.
#
# Тесты, в рамках которых необходимо рассмотреть как можно больше краевых кейсов.


# Узел дерева
class TreeNode:
    # Конструктор
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Проверка дерева на сбалансированность
def is_balanced(root):
    # Внутренняя функция для рекурсивных вызовов
    def check_balance(node):
        if not node:
            return True, 0
        # Проверка левого поддерева
        left_balanced, left_height = check_balance(node.left)
        if not left_balanced:
            return False, 0
        # Проверка правого поддерева
        right_balanced, right_height = check_balance(node.right)
        if not right_balanced:
            return False, 0
        # Проверка разницы высот
        balanced = abs(left_height - right_height) <= 1
        height = 1 + max(left_height, right_height)
        # Результат
        return balanced, height
    return check_balance(root)[0]


# Старт программы
if __name__ == "__main__":
    # Примеры использования

    # Пустое дерево
    print(is_balanced(None))  # True

    # Один узел
    print(is_balanced(TreeNode(5)))  # True

    # Сбалансированное дерево
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    print(is_balanced(root))  # True

    # Несбалансированное дерево
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.left.left = TreeNode(4)
    print(is_balanced(root))  # False

    # Дерево с разной высотой поддеревьев
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.right = TreeNode(3)
    print(is_balanced(root))  # False

    # Сбалансированное дерево с несколькими уровнями
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(15)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(7)
    root.right.right = TreeNode(20)
    print(is_balanced(root))  # True

    # Крайний случай с нулевыми значениями
    root = TreeNode(0)
    root.left = TreeNode(0)
    root.right = TreeNode(0)
    print(is_balanced(root))  # True

    # Сложная несбалансированная структура
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.left.left = TreeNode(4)
    root.right = TreeNode(5)
    root.right.right = TreeNode(6)
    print(is_balanced(root))  # False
