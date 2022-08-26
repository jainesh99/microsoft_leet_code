def fib(n: int) -> int:

    table = [0] * (n + 1)
    table[1] = 1

    for i in range(1, n):

        table[i + 1] += table[i]

        if i + 2 <= n:
            table[i + 2] += table[i]
    return table[n]


print(fib(6))
print(fib(7))
print(fib(8))
print(fib(50))
