from collections import deque


def bfs_shortest_path(graph, start, goal):
    visited = set()
    queue = deque([[start]])

    if start == goal:
        return [start]

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node not in visited:
            neighbors = graph[node]

            for neighbor in neighbors:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)

                if neighbor == goal:
                    return new_path

            visited.add(node)

    return []

def dfs_depth_search(graph, start, depth, visited=None):
    if visited is None:
        visited = set()

    if depth < 0:
        return visited

    visited.add(start)

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs_depth_search(graph, neighbor, depth - 1, visited)

    return visited