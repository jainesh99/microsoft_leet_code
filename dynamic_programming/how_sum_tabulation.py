from typing import List


def how_sum(target: int, numbers: List[int]) -> int:

    table_length = target + 1

    table = [None] * table_length
    table[0] = []

    for i in range(table_length):

        if table[i] is not None:

            for number in numbers:
                forward_index = i + number
                if forward_index < table_length:
                    table[forward_index] = [number]

                    if len(table[i]) > 0:
                        table[forward_index] = table[forward_index] + table[i]

    return table[target]


print(how_sum(7, [5, 3, 4]))
print(how_sum(7, [2, 3]))
print(how_sum(7, [5, 3, 4, 7]))
print(how_sum(7, [2, 4]))
print(how_sum(8, [2, 3, 5]))
print(how_sum(300, [7, 14]))
