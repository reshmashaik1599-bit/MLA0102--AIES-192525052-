def minimax(depth, node, maximizing, values, alpha, beta):

    if depth == 3:
        return values[node]

    if maximizing:
        best = float('-inf')

        for child in range(2):
            value = minimax(
                depth + 1,
                node * 2 + child,
                False,
                values,
                alpha,
                beta
            )

            best = max(best, value)
            alpha = max(alpha, best)

            if beta <= alpha:
                print("Pruned node:", node * 2 + child)
                break

        return best

    else:
        best = float('inf')

        for child in range(2):
            value = minimax(
                depth + 1,
                node * 2 + child,
                True,
                values,
                alpha,
                beta
            )

            best = min(best, value)
            beta = min(beta, best)

            if beta <= alpha:
                print("Pruned node:", node * 2 + child)
                break

        return best


values = {
    7: 3,
    8: 5,
    9: 2,
    10: 9,
    11: 12,
    12: 5,
    13: 23,
    14: 23
}

result = minimax(
    0, 0, True, values,
    float('-inf'),
    float('inf')
)

print("Best value:", result)