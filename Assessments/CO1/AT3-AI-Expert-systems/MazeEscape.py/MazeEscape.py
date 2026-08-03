from collections import deque

# Maze representation
# 0 = Open path
# 1 = Wall

maze = [
    [0, 0, 1, 0, 0],
    [0, 0, 1, 0, 1],
    [1, 0, 0, 0, 1],
    [1, 1, 1, 0, 0],
    [1, 1, 1, 1, 0]
]

ROWS = len(maze)
COLS = len(maze[0])

start = (0, 0)
goal = (4, 4)

directions = [
    (-1, 0),  # Up
    (1, 0),   # Down
    (0, -1),  # Left
    (0, 1)    # Right
]


def bfs():
    queue = deque()
    queue.append(start)

    visited = set()
    visited.add(start)

    parent = {}

    while queue:
        current = queue.popleft()

        if current == goal:
            path = []

            while current != start:
                path.append(current)
                current = parent[current]

            path.append(start)
            path.reverse()
            return path

        for dx, dy in directions:
            nx = current[0] + dx
            ny = current[1] + dy

            if 0 <= nx < ROWS and 0 <= ny < COLS:
                if maze[nx][ny] == 0 and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    parent[(nx, ny)] = current
                    queue.append((nx, ny))

    return None


def display_maze(path):
    print("\nMaze:\n")

    for i in range(ROWS):
        for j in range(COLS):

            if (i, j) == start:
                print("S", end=" ")

            elif (i, j) == goal:
                print("G", end=" ")

            elif maze[i][j] == 1:
                print("#", end=" ")

            elif (i, j) in path:
                print("*", end=" ")

            else:
                print(".", end=" ")
        print()


path = bfs()

if path:
    display_maze(path)

    print("\nShortest Path:")
    for node in path:
        print(node)

    print("\nTotal Steps =", len(path) - 1)

else:
    print("No path found.")