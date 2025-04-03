import heapq

def dijkstra(graph, start, end):
    """
    Находит кратчайшее расстояние от start до end в ориентированном взвешенном графе,
    используя алгоритм Дейкстры.

    Args:
        graph: Матрица смежности, представленная в виде списка списков.
               graph[i][j] - вес ребра от i к j, или -1, если ребра нет.
               Нумерация вершин от 0 до N-1.
        start: Начальная вершина (нумерация от 0).
        end: Конечная вершина (нумерация от 0).

    Returns:
        Кратчайшее расстояние от start до end, или -1, если пути не существует.
    """

    n = len(graph)
    dist = [float('inf')] * n  # Инициализируем расстояния бесконечностью
    dist[start] = 0  # Расстояние до начальной вершины равно 0

    pq = [(0, start)]  # Очередь с приоритетами: (расстояние, вершина)
    heapq.heapify(pq)

    while pq:
        d, u = heapq.heappop(pq)  # Извлекаем вершину с наименьшим расстоянием

        if d > dist[u]:
            continue  # Если расстояние до вершины u уже меньше, чем текущее, пропускаем

        for v in range(n):
            weight = graph[u][v]
            if weight != -1:  # Если есть ребро между u и v
                if dist[v] > dist[u] + weight:
                    dist[v] = dist[u] + weight
                    heapq.heappush(pq, (dist[v], v))  # Добавляем вершину v в очередь с приоритетами

    if dist[end] == float('inf'):
        return -1  # Пути не существует
    else:
        return dist[end]


def solve_dijkstra_from_file(input_file="input3.txt", output_file="output3.txt"):
    """
    Решает задачу поиска кратчайшего пути в графе, считывая данные из файла и выводя результат в файл.

    Args:
        input_file: Имя входного файла. Первая строка содержит N, S, F.
                   Следующие N строк содержат матрицу смежности.
        output_file: Имя выходного файла, в который будет записан результат.
    """

    try:
        with open(input_file, "r") as f_in:
            n, start, end = map(int, f_in.readline().split())
            start -= 1  # Переходим к 0-индексации
            end -= 1  # Переходим к 0-индексации
            graph = []
            for _ in range(n):
                row = list(map(int, f_in.readline().split()))
                graph.append(row)

    except FileNotFoundError:
        print(f"Ошибка: Файл {input_file} не найден.")
        return
    except ValueError:
        print(f"Ошибка: Некорректный формат входных данных в файле {input_file}.")
        return
    except Exception as e:
        print(f"Ошибка: Произошла ошибка при чтении файла: {e}")
        return

    result = dijkstra(graph, start, end)

    try:
        with open(output_file, "w") as f_out:
            f_out.write(str(result) + "\n")

    except Exception as e:
        print(f"Ошибка: Произошла ошибка при записи в файл: {e}")
        return


if __name__ == "__main__":
    solve_dijkstra_from_file()