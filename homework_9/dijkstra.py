# Реализовать алгоритм Дейкстры для взвешенного графа.

import heapq


# Алгоритм Дейкстры для взвешенного графа
def dijkstra(graph, start):
    # Инициализация
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    visited = set()
    priority_queue = [(0, start)]  # (расстояние, вершина)

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # Если вершина уже обработана, пропускаем
        if current_vertex in visited:
            continue

        visited.add(current_vertex)

        # Обновление расстояний для соседей
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            # Если найден более короткий путь
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


# Старт программы
if __name__ == "__main__":
    # Тесты

    # Простой граф
    graph = {'A': {'B': 1, 'C': 4}, 'B': {'C': 2}, 'C': {}}
    print(dijkstra(graph, 'A'))  # {'A': 0, 'B': 1, 'C': 3}

    # Граф с циклами
    graph = {'A': {'B': 1, 'C': 4}, 'B': {'C': 2, 'A': 2}, 'C': {'A': 1}}
    result = dijkstra(graph, 'A')
    print(result['C'])  # 3

    # Граф с изолированной вершиной
    graph = {'A': {'B': 1}, 'B': {}, 'C': {}}
    result = dijkstra(graph, 'A')
    print(result['C'])  # inf

    # Граф с одинаковыми весами рёбер
    graph = {'A': {'B': 1, 'C': 1}, 'B': {'D': 1}, 'C': {'D': 1}, 'D': {}}
    result = dijkstra(graph, 'A')
    print(result['D'])  # 2

    # Проверка на отсутствие путей
    graph = {'A': {'B': 1}, 'B': {}, 'C': {'D': 1}, 'D': {}}
    result = dijkstra(graph, 'A')
    print(result['C'] == float('infinity') and result['D'] == float('infinity'))  # True

    # Одиночная вершина
    graph = {'A': {}}
    print(dijkstra(graph, 'A'))  # {'A': 0}
