



def min_cost_climbing_stairs(cost):

    # Initialize the minimum cost to reach the top of the floor
    # as the minimum of the cost of the first and second step
    min_cost = min(cost[0], cost[1])

    first = cost[0]
    second = cost[1]

    for i in range(2, len(cost)):
        min_cost = min(first, second) + cost[i]
        first = second
        second = min_cost

    return min(first, second)
