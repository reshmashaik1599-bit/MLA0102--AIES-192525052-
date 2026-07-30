def minimax(depth, nodeIndex, isMax, values, maxDepth):

    # Base case: Leaf node reached
    if depth == maxDepth:
        return values[nodeIndex]

    if isMax:
        return max(
            minimax(depth + 1, nodeIndex * 2, False, values, maxDepth),
            minimax(depth + 1, nodeIndex * 2 + 1, False, values, maxDepth)
        )
    else:
        return min(
            minimax(depth + 1, nodeIndex * 2, True, values, maxDepth),
            minimax(depth + 1, nodeIndex * 2 + 1, True, values, maxDepth)
        )


# Leaf node values
values = [3, 5, 2, 9, 12, 5, 23, 23]

maxDepth = 3

result = minimax(0, 0, True, values, maxDepth)

print("The optimal value is:", result)