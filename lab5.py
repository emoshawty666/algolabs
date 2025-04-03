from collections import deque

def bfs(graph, start, finish):
  """
  Выполняет поиск в ширину (BFS) для нахождения кратчайшего пути в графе.

  Args:
    graph: Словарь, представляющий граф. Ключи - узлы, значения - строка соседних узлов.
    start: Начальный узел.
    finish: Конечный узел.

  Returns:
    Кортеж: (длина кратчайшего пути, строка пути), или (None, None), если путь не найден.
  """

  distance = {node: -1 for node in graph}
  distance[start] = 0

  prev = {start: '$'} # '$' is used as a marker for the initial state, equivalent to C++'s '$'

  q = deque([start])

  while q:
    from_node = q.popleft()
    for to_node in graph[from_node]:
      if distance[to_node] == -1:
        q.append(to_node)
        distance[to_node] = distance[from_node] + 1
        prev[to_node] = from_node

  if distance[finish] == -1:
    return None, None  # No path found

  # Reconstruct path
  current = finish
  path = current
  while prev[current] != '$':
    current = prev[current]
    path += current

  return distance[finish], path[::-1]  # Reverse the path for correct order


if __name__ == "__main__":
  graph = {
      'H': 'IGF',
      'I': 'HJ',
      'F': 'HG',
      'G': 'FHJ',
      'J': 'IGC',
      'E': 'GAS',
      'A': 'ES',
      'S': 'AEDB',
      'D': 'SB',
      'B': 'SDC',
      'C': 'BJ'
  }

  start = 'S'
  finish = 'I'

  distance, path = bfs(graph, start, finish)

  if distance is not None:
    print(distance)
    print(path)
  else:
    print("No path found.")