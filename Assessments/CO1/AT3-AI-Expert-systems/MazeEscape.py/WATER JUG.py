from collections import deque

# Jug capacities
JUG1 = 11
JUG2 = 9
GOAL = 8

# BFS Function
def bfs():
    visited = set()
    queue = deque()

    # Initial state (Jug1, Jug2)
    queue.append(((0, 0), []))
    visited.add((0, 0))

    while queue:
        (a, b), path = queue.popleft()

        # Goal Check
        if a == GOAL or b == GOAL:
            return path + [(a, b)]

        next_states = []

        # Fill Jug1
        next_states.append((JUG1, b))

        # Fill Jug2
        next_states.append((a, JUG2))

        # Empty Jug1
        next_states.append((0, b))

        # Empty Jug2
        next_states.append((a, 0))

        # Pour Jug1 -> Jug2
        transfer = min(a, JUG2 - b)
        next_states.append((a - transfer, b + transfer))

        # Pour Jug2 -> Jug1
        transfer = min(b, JUG1 - a)
        next_states.append((a + transfer, b - transfer))

        for state in next_states:
            if state not in visited:
                visited.add(state)
                queue.append((state, path + [(a, b)]))

    return None


# Run BFS
solution = bfs()

print("\n========== WATER JUG PUZZLE ==========\n")
print("Jug Capacities: 11L and 9L")
print("Goal: Measure exactly 8 Litres\n")

if solution:
    print("Solution Found!\n")

    for i, state in enumerate(solution):
        print(f"Step {i}: Jug1 = {state[0]}L, Jug2 = {state[1]}L")

    print("\nGoal Achieved!")
    print("One of the jugs contains exactly 8 litres.")
else:
    print("No Solution Exists.")