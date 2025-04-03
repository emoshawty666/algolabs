import heapq

def solve_gas_problem(input_file="input4.txt", output_file="output4.txt"):
    try:
        with open(input_file, "r") as f_in:
            n = int(f_in.readline().strip())
            costs = list(map(int, f_in.readline().split()))
            m = int(f_in.readline().strip())
            graph = [[] for _ in range(n)]  # Список смежности
            for _ in range(m):
                a, b = map(int, f_in.readline().split())
                a -= 1  # Переходим к 0-индексации
                b -= 1  # Переходим к 0-индексации
                graph[a].append(b)
                graph[b].append(a)

    except FileNotFoundError:
        print(f"Ошибка: Файл {input_file} не найден.")
        return
    except ValueError:
        print(f"Ошибка: Некорректный формат входных данных в файле {input_file}.")
        return
    except Exception as e:
        print(f"Ошибка: Произошла ошибка при чтении файла: {e}")
        return

    start = 0  # Начальный город (0-индексация)
    end = n - 1  # Конечный город (0-индексация)

    # Алгоритм Дейкстры с использованием стоимости бензина в качестве веса ребер
    dist = [float('inf')] * n
    dist[start] = 0

    pq = [(0, start)]  # (стоимость, город)
    heapq.heapify(pq)

    while pq:
        d, u = heapq.heappop(pq)

        if d > dist[u]:
            continue

        for v in graph[u]:
            weight = costs[v]  # Стоимость бензина в городе v
            if dist[v] > dist[u] + weight:
                dist[v] = dist[u] + weight
                heapq.heappush(pq, (dist[v], v))

    result = dist[end] if dist[end] != float('inf') else -1

    try:
        with open(output_file, "w") as f_out:
            f_out.write(str(result) + "\n")

    except Exception as e:
        print(f"Ошибка: Произошла ошибка при записи в файл: {e}")
        return


if __name__ == "__main__":
    solve_gas_problem()