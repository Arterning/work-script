def minCoins(coins, amount):
    # 创建一个dp数组，dp[i]表示凑出金额i所需的最少硬币数量，初始化为无穷大
    dp = [float('inf')] * (amount + 1)

    # 凑出金额0需要0个硬币
    dp[0] = 0

    for coin in coins:
        for i in range(coin, amount + 1):
            # 状态转移方程：dp[i] = min(dp[i], dp[i - coin] + 1)
            dp[i] = min(dp[i], dp[i - coin] + 1)

    # 如果dp[amount]仍然是无穷大，说明无法凑出该金额，返回-1
    if dp[amount] == float('inf'):
        return -1

    return dp[amount]


coins = [8, 3, 5]
amount = 11
result = minCoins(coins, amount)
print(f"最少需要的硬币数量：{result}")
