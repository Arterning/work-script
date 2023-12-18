def fibonacci(n):
    if n <= 1:
        return n

    fib = [0] * (n + 1)
    fib[1] = 1

    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]

    return fib[n]


n = 10  # 你可以更改 n 来计算不同项的斐波那契数列
result = fibonacci(n)
print(f"斐波那契数列的第 {n} 项是 {result}")
