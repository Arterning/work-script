def knapsack(weights, values, capacity):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]

    # 从dp表中找出选择的物品
    selected_items = []
    i, j = n, capacity
    while i > 0 and j > 0:
        if dp[i][j] != dp[i - 1][j]:
            selected_items.append(i - 1)
            j -= weights[i - 1]
        i -= 1

    selected_weights = [weights[i] for i in selected_items]
    selected_values = [values[i] for i in selected_items]
    total_value = dp[n][capacity]

    return {
        "选择的物品": selected_weights,
        "物品的总价值": total_value
    }


weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
capacity = 5
result = knapsack(weights, values, capacity)
print(result)
