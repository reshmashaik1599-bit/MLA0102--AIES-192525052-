# Alpha-Beta Pruning Implementation

def alpha_beta(depth, node_index, maximizing_player, values, alpha, beta):
    
    # Leaf node reached
    if depth == 0:
        return values[node_index]

    if maximizing_player:
        best = -float('inf')

        # MAX player
        for i in range(2):
            value = alpha_beta(depth-1, node_index*2+i,
                               False, values, alpha, beta)
            best = max(best, value)
            alpha = max(alpha, best)

            # Beta cutoff
            if beta <= alpha:
                break

        return best

    else:
        best = float('inf')

        # MIN player
        for i in range(2):
            value = alpha_beta(depth-1, node_index*2+i,
                               True, values, alpha, beta)
            best = min(best, value)
            beta = min(beta, best)

            # Alpha cutoff
            if beta <= alpha:
                break

        return best


# Input leaf node values
values = [3, 5, 6, 9, 1, 2, 0, -1]

# Depth of tree
depth = 3

# Initial alpha and beta values
alpha = -float('inf')
beta = float('inf')

# Find optimal value
result = alpha_beta(depth, 0, True, values, alpha, beta)

print("Optimal value:", result)