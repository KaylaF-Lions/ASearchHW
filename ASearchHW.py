import heapq

def a_star(graph, heuristics, start, goal):
    queue = [(heuristics[start], start, [start], 0)]
    visited = set()

    while queue:
        f, current, path, g = heapq.heappop(queue)

        if current == goal:
            return path, g

        if current in visited:
            continue
        visited.add(current)

        for neighbor, cost in graph[current].items():
            if neighbor not in visited:
                new_g = g + cost
                new_f = new_g + heuristics[neighbor]
                heapq.heappush(queue, (new_f, neighbor, path + [neighbor], new_g))

    return None, float('inf')

graph = {
    'S': {'A': 3, 'B': 2, 'C': 5},
    'A': {'G': 2, 'C': 3, 'H': 4},
    'B': {'D': 6},
    'C': {'B': 4, 'H': 3},
    'D': {'E': 2, 'F': 3},
    'G': {'E': 5, 'D': 4},
    'H': {'D': 4},
    'E': {'F': 5},
    'F': {}
}

heuristics = {
    'S': 10, 'A': 8, 'B': 9, 'C': 7, 'G': 6, 'H': 6, 'D': 4, 'E': 3, 'F': 0
}

path, cost = a_star(graph, heuristics, 'S', 'F')
print("Path:", " -> ".join(path))
print("Total Cost:", cost)