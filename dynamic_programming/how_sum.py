from typing import Dict, List


def how_sum(targetSum: int, numbers: List[int], memo: Dict = None):
    if memo is None:
        memo = {}

    if targetSum in memo.keys():
        return memo[targetSum]

    if targetSum == 0:
        return []

    if targetSum < 0:
        return None

    for number in numbers:
        return_arr = how_sum(targetSum - number, numbers, memo)

        if return_arr is not None:
            return_arr.append(number)
            memo[targetSum] = return_arr
            return memo[targetSum]

    memo[targetSum] = None
    return None


print(how_sum(7, [2, 3]))
print(how_sum(7, [5, 3, 4, 7]))
print(how_sum(7, [2, 4]))
print(how_sum(8, [2, 3, 5]))
print(how_sum(300, [7, 14]))
