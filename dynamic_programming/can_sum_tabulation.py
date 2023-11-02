from typing import List


def can_sum(target_sum: int, numbers: List[int]) -> bool:
    number_of_items = target_sum + 1

    table = [False] * number_of_items
    table[0] = True

    for i in range(number_of_items):
        if table[i]:
            for number in numbers:
                if i + number < number_of_items:
                    table[i + number] = True

    return table[target_sum]


print(can_sum(7, [2, 3]))
print(can_sum(7, [5, 3, 4, 7]))
print(can_sum(7, [2, 4]))
print(can_sum(8, [2, 3, 5]))
print(can_sum(300, [7, 14]))
