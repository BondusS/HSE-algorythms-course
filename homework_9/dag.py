# Дан ориентированный граф.
# 1) Нужно определить, есть ли в графе цикл
# 2) Если цикл есть - вывести его (достаточно одного цикла)
# 3) Если цикла нет - применяем топологическую сортировку и выводим результат
# Подразумевается, что граф подается на вход в виде списка смежности (словарь со списками ребер).

from collections import defaultdict, deque


# Поиск циклов и топологическая сортировка
def find_cycle_or_topsort(graph):
    n = len(graph)
    used = [0] * n  # 0 — белый, 1 — серый, 2 — чёрный
    path = []
    cycle = []

    # Поиск в глубину
    def dfs(v):
        used[v] = 1
        path.append(v)
        for to in graph[v]:
            if used[to] == 1:
                # Найден цикл
                idx = path.index(to)
                for ind in path[idx:]:
                    cycle.append(ind)
                return True
            if used[to] == 0 and dfs(to):
                return True
        used[v] = 2
        path.pop()
        return False

    # Ищем цикл
    for v in range(n):
        if used[v] == 0 and dfs(v):
            return "Цикл найден:", cycle

    # Если цикла нет — топологическая сортировка
    in_degree = [0] * n
    for v in graph:
        for to in graph[v]:
            in_degree[to] += 1

    queue = deque([v for v in range(n) if in_degree[v] == 0])
    topsort = []

    while queue:
        v = queue.popleft()
        topsort.append(v)
        for to in graph[v]:
            in_degree[to] -= 1
            if in_degree[to] == 0:
                queue.append(to)

    return "Топологическая сортировка:", topsort


# Старт программы
if __name__ == "__main__":
    # Тесты

    # Граф без рёбер (изолированные вершины)
    graph = {0: [], 1: [], 2: []}
    print(find_cycle_or_topsort(graph))  # ('Топологическая сортировка:', [0, 1, 2])

    # Длинный ациклический путь (линейный граф)
    graph = {0: [1], 1: [2], 2: [3], 3: [4], 4: []}
    print(find_cycle_or_topsort(graph))  # ('Топологическая сортировка:', [0, 1, 2, 3, 4])

    # Граф с несколькими циклами
    graph = {
        0: [1], 1: [2], 2: [0],  # цикл 0-1-2-0
        3: [4], 4: [3]  # цикл 3-4-3
    }
    print(find_cycle_or_topsort(graph))  # ('Цикл найден:', [0, 1, 2])

    # Простой цикл из двух вершин
    graph = {0: [1], 1: [0]}
    print(find_cycle_or_topsort(graph))  # ('Цикл найден:', [0, 1])

    # Сложный ациклический граф (дерево)
    graph = {
        0: [1, 2],
        1: [3, 4],
        2: [5],
        3: [], 4: [], 5: []
    }
    print(find_cycle_or_topsort(graph))  # ('Топологическая сортировка:', [0, 1, 2, 3, 4, 5])

    # Граф с рёбрами, образующими «двойной цикл» (пересекающиеся циклы)
    graph = {
        0: [1], 1: [2], 2: [0],  # цикл 0-1-2-0
        1: [3], 3: [4], 4: [1]  # цикл 1-3-4-1
    }
    print(find_cycle_or_topsort(graph))  # ('Цикл найден:', [1, 3, 4])
