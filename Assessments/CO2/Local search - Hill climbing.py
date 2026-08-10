def hill_climbing(start, goal, graph, heuristic):

    current = start
    path = [current]

    while current != goal:

        neighbours = graph[current]

        if not neighbours:
            print("No path to goal")
            return

        next_node = min(
            neighbours,
            key=lambda x: heuristic[x]
        )

        if heuristic[next_node] >= heuristic[current]:
            print("Local optimum reached")
            return

        current = next_node
        path.append(current)

        print("Move to:", current)

    print("Goal reached!")
    print("Path:", path)


graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': ['G'],
    'E': ['G'],
    'F': ['G'],
    'G': []
}

heuristic = {
    'A': 7,
    'B': 5,
    'C': 4,
    'D': 2,
    'E': 3,
    'F': 1,
    'G': 0
}

hill_climbing('A', 'G', graph, heuristic)