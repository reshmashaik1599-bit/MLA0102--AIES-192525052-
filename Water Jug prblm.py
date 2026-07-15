from collections import deque

def water_jug(cap1, cap2, target):
    visited = set()
    queue = deque([((0, 0), [])])

    while queue:
        (x, y), path = queue.popleft()

        if (x, y) in visited:
            continue

        visited.add((x, y))
        path = path + [(x, y)]

        # Check if the target is reached
        if x == target or y == target:
            print("Steps to reach the goal:")
            for state in path:
                print(state)
            return

        # Generate all possible next states
        next_states = [
            (cap1, y),                                # Fill Jug 1
            (x, cap2),                                # Fill Jug 2
            (0, y),                                   # Empty Jug 1
            (x, 0),                                   # Empty Jug 2
            (x - min(x, cap2 - y), y + min(x, cap2 - y)),  # Pour Jug 1 into Jug 2
            (x + min(y, cap1 - x), y - min(y, cap1 - x))   # Pour Jug 2 into Jug 1
        ]

        for state in next_states:
            if state not in visited:
                queue.append((state, path))

    print("No solution exists.")

# Main Program
jug1 = 5
jug2 = 3
goal = 4

water_jug(jug1, jug2, goal)