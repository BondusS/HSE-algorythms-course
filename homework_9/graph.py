# Дан неориентированный граф.
# Необходимо, найти все компоненты связности графа и вывести их.
# Подразумевается, что граф подается на вход в виде списка смежности (словарь со списками ребер).
# Здесь очень важны краевые случаи. Тесты должны их покрыть.


# Находит все компоненты связности неориентированного графа
def find_connected_components(graph):

    # аргументы:
    #     graph: словарь, представляющий список смежности графа
    #            ключи — вершины, значения — списки смежных вершин
    # возвращает:
    #     список множеств, каждое из которых представляет компоненту связности

    visited = set()
    components = []

    # Рекурсивный DFS для обхода компоненты связности
    def dfs(vertex, component):
        visited.add(vertex)
        component.add(vertex)
        for neighbor in graph.get(vertex, []):
            if neighbor not in visited:
                dfs(neighbor, component)

    for vertex in graph:
        if vertex not in visited:
            component = set()
            dfs(vertex, component)
            components.append(component)

    return components


# Старт программы
if __name__ == "__main__":
    # Тесты

    # Связный граф
    graph = {1: [2, 3], 2: [1, 4], 3: [1], 4: [2]}
    print(find_connected_components(graph))  # [{1, 2, 3, 4}]

    # Граф с двумя компонентами
    graph = {1: [2], 2: [1], 3: [4], 4: [3]}
    print(find_connected_components(graph))  # [{1, 2}, {3, 4}]

    # Изолированные вершины
    graph = {1: [], 2: [], 3: []}
    print(find_connected_components(graph))  # [{1}, {2}, {3}]

    # Пустой граф
    graph = {}
    print(find_connected_components(graph))  # []

    # Граф с компонентами разной мощности
    graph = {1: [2], 2: [1], 3: [4, 5], 4: [3], 5: [3]}
    print(find_connected_components(graph))  # [{1, 2}, {3, 4, 5}]

    # Граф с петлёй
    graph = {1: [1, 2], 2: [1]}
    print(find_connected_components(graph))  # [{1, 2}]
