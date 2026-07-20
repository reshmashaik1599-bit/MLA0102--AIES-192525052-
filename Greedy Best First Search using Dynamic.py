# Greedy Best First Search using Dynamic Input

import heapq

graph = {}
heuristic = {}

n = int(input("Enter number of nodes: "))

print("Enter node names:")
nodes = []
for i in range(n):
    node = input()
    nodes.append(node)
    graph[node] = []

print("\nEnter heuristic values:")
for node in nodes:
    heuristic[node] = int(input(f"Heuristic of {node}: "))

e = int(input("\nEnter number of edges: "))

print("Enter edges (Source Destination Cost):")
for i in range(e):
    u, v, cost = input().split()
    graph[u].append((v, int(cost)))
    graph[v].append((u, int(cost)))

start = input("\nEnter start node: ")
goal = input("Enter goal node: ")

visited = set()
pq = []
heapq.heappush(pq, (heuristic[start], start))
path = []

while pq:
    h, node = heapq.heappop(pq)

    if node not in visited:
        visited.add(node)
        path.append(node)

        if node == goal:
            break

        for neighbor, cost in graph[node]:
            if neighbor not in visited:
                heapq.heappush(pq, (heuristic[neighbor], neighbor))

print("\nPath:", " -> ".join(path))