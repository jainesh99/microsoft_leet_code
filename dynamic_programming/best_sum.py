from typing import Dict, List


def best_sum(target_sum: int, numbers: List[int], memo: [Dict] = None) -> List[int]:

    if memo is None:
        memo = {}

    if target_sum in memo.keys():
        return memo[target_sum]

    shortest_sum = None

    if target_sum == 0:
        return []

    if target_sum < 0:
        return None

    for number in numbers:

        sum_arr = best_sum(target_sum - number, numbers, memo)

        if sum_arr is not None:

            sum_arr.append(number)

            if shortest_sum is None or len(sum_arr) < len(shortest_sum):
                shortest_sum = sum_arr.copy()

    memo[target_sum] = shortest_sum

    return shortest_sum


print(best_sum(8, [2, 3, 5]))
print(best_sum(7, [5, 3, 4, 7]))
print(best_sum(100, [25, 1, 2, 5]))
