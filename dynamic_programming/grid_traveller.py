def gridTraveller(m: int, n: int, memo=None) -> int:
    if memo is None:
        memo = {}

    if m == 1 and n == 1:
        return 1

    if m == 0 or n == 0:
        return 0

    if (m, n) in memo.keys():
        return memo[(m, n)]

    memo[(m, n)] = gridTraveller(m - 1, n, memo) + gridTraveller(m, n - 1, memo)
    return memo[(m, n)]


print(gridTraveller(1, 1))
print(gridTraveller(2, 3))
print(gridTraveller(3, 2))
print(gridTraveller(3, 3))
print(gridTraveller(18, 18))
