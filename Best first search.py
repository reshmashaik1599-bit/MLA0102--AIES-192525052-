from queue import PriorityQueue

graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 2), ('E', 4)],
    'C': [('F', 2)],
    'D': [],
    'E': [('G', 1)],
    'F': [('G', 2)],
    'G': []
}

def best_first_search(start, goal):
    visited = set()
    pq = PriorityQueue()

    pq.put((0, start))

    while not pq.empty():
        h, node = pq.get()

        if node in visited:
            continue

        print(node, end=" ")
        visited.add(node)

        if node == goal:
            print("\nGoal Found!")
            return

        for neighbour, heuristic in graph[node]:
            if neighbour not in visited:
                pq.put((heuristic, neighbour))

start = input("Enter Start Node: ")
goal = input("Enter Goal Node: ")

best_first_search(start, goal)