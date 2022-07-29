from typing import List


def can_sum(target_sum: int, numbers: List[int], memo=None) -> bool:

    if memo is None:
        memo = {}

    if target_sum in memo.keys():
        return memo[target_sum]

    if target_sum == 0:
        return True

    if target_sum < 0:
        return False

    for number in numbers:
        if can_sum(target_sum - number, numbers, memo):
            memo[target_sum] = True
            return True

    memo[target_sum] = False
    return False


print(can_sum(7, [2, 3]))
print(can_sum(7, [5, 3, 4, 7]))
print(can_sum(7, [2, 4]))
print(can_sum(8, [2, 3, 5]))
print(can_sum(300, [7, 14]))
