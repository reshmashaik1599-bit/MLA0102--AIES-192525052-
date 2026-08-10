# A* Search using Dynamic Input

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

pq = []
heapq.heappush(pq, (heuristic[start], 0, start, [start]))

visited = set()

while pq:
    f, g, node, path = heapq.heappop(pq)

    if node == goal:
        print("\nOptimal Path:", " -> ".join(path))
        print("Optimal Cost:", g)
        break

    if node in visited:
        continue

    visited.add(node)

    for neighbor, cost in graph[node]:
        if neighbor not in visited:
            new_g = g + cost
            new_f = new_g + heuristic[neighbor]
            heapq.heappush(pq, (new_f, new_g, neighbor, path + [neighbor]))