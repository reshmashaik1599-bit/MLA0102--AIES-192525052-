from queue import PriorityQueue

# Graph represented as an adjacency list
graph = {
    'A': [('B', 2), ('C', 4)],
    'B': [('D', 3), ('E', 5)],
    'C': [('F', 6)],
    'D': [],
    'E': [('F', 1)],
    'F': []
}

# Uniform Cost Search function
def uniform_cost_search(graph, start, goal):
    pq = PriorityQueue()
    pq.put((0, start, [start]))  # (cost, current node, path)
    visited = set()

    while not pq.empty():
        cost, node, path = pq.get()

        if node == goal:
            return path, cost

        if node not in visited:
            visited.add(node)

            for neighbor, weight in graph[node]:
                if neighbor not in visited:
                    pq.put((cost + weight, neighbor, path + [neighbor]))

    return None

# Main Program
start = 'A'
goal = 'F'

result = uniform_cost_search(graph, start, goal)

if result:
    path, cost = result
    print("Least Cost Path:", " -> ".join(path))
    print("Total Cost:", cost)
else:
    print("No path found.")