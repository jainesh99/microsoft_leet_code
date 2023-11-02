from typing import List


class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        num_of_rows = len(grid)
        num_of_columns = len(grid[0])

        remaining = k % num_of_columns
        temp = []

        if k >= num_of_columns:
            for _ in range(k // num_of_columns):
                bottom_row = grid.pop(num_of_rows - 1)
                grid.insert(0, bottom_row)

        for _ in range(remaining):
            for i in range(num_of_rows - 1, -1, -1):
                temp.append(grid[i].pop(num_of_columns - 1))

            grid[0].insert(0, temp.pop(0))

            for i in range(num_of_rows - 1, 0, -1):
                grid[i].insert(0, temp.pop(0))

        return grid


solution = Solution()
grid = [
    [-353, 853, 839, 122, -337],
    [819, 356, 116, 0, 791],
    [-516, -502, -681, -427, -314],
    [-386, -400, 597, 740, 836],
    [129, 598, 40, -875, -968],
    [495, -604, 79, 414, -104],
    [237, 121, 211, 4, 677],
    [-712, 351, -947, -203, 361],
]
k = 7
print(solution.shiftGrid(grid, k))

# [[4,677,-712,351,-947],
# [-203,361,-353,853,839],
# [122,-337,819,356,116],
# [0,791,-516,-502,-681],
# [-427,-314,-386,-400,597],
# [740,836,129,598,40],
# [-875,-968,495,-604,79],
# [414,-104,237,121,211]]
