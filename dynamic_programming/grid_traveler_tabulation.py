def grid_traveler(m: int, n: int) -> int:
    grid = [[0] * (n + 1) for i in range(m + 1)]

    grid[1][1] = 1

    for row in range(m + 1):
        for col in range(n + 1):
            if col + 1 <= n:
                grid[row][col + 1] += grid[row][col]

            if row + 1 <= m:
                grid[row + 1][col] += grid[row][col]

    return grid[m][n]


print(grid_traveler(1, 1))
print(grid_traveler(2, 3))
print(grid_traveler(3, 2))
print(grid_traveler(3, 3))
print(grid_traveler(18, 18))
