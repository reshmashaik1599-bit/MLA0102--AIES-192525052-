from heapq import heappush, heappop

GOAL = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

START = [
    [1, 2, 3],
    [4, 0, 6],
    [7, 5, 8]
]


# Find blank tile
def find_zero(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j


# Heuristic (Misplaced Tiles)
def heuristic(state):
    count = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0 and state[i][j] != GOAL[i][j]:
                count += 1
    return count


# Generate next states
def neighbors(state):
    x, y = find_zero(state)

    moves = [(-1,0),(1,0),(0,-1),(0,1)]

    result = []

    for dx, dy in moves:
        nx = x + dx
        ny = y + dy

        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [row[:] for row in state]

            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]

            result.append(new_state)

    return result


# Convert board to tuple
def board_tuple(state):
    return tuple(tuple(r) for r in state)


# Print board
def print_board(state):
    for row in state:
        print(row)
    print()


# A* Search
def astar(start):

    pq = []

    heappush(pq, (heuristic(start), 0, start, []))

    visited = set()

    while pq:

        f, g, current, path = heappop(pq)

        if current == GOAL:
            return path + [current]

        key = board_tuple(current)

        if key in visited:
            continue

        visited.add(key)

        for nxt in neighbors(current):

            if board_tuple(nxt) not in visited:

                heappush(
                    pq,
                    (
                        g + 1 + heuristic(nxt),
                        g + 1,
                        nxt,
                        path + [current]
                    )
                )

    return None


print("\n========== 8 PUZZLE USING A* SEARCH ==========\n")

print("Initial State\n")
print_board(START)

solution = astar(START)

if solution:

    print("Solution Found!\n")

    for step, state in enumerate(solution):

        print("Step", step)

        print_board(state)

    print("Goal State Reached!")
    print("Total Moves =", len(solution)-1)

else:

    print("No Solution Found.")