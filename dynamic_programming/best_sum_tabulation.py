from typing import List


def best_sum(target: int, numbers: List[int]):

    table_length = target + 1
    table: List = [None] * table_length
    table[0] = []

    for index in range(len(table)):

        for number in numbers:

            if isinstance(table[index], list):

                if index + number < table_length:

                    list_of_numbers: List = table[index].copy()
                    list_of_numbers.append(number)

                    if table[index + number]:

                        if len(table[index + number]) > len(list_of_numbers):

                            table[index + number] = list_of_numbers.copy()
                    else:
                        table[index + number] = list_of_numbers.copy()

    return table[target]


print(best_sum(7, [5, 3, 4, 7]))
print(best_sum(8, [2, 3, 5]))
print(best_sum(8, [1, 4, 5]))
print(best_sum(100, [25, 1, 2, 5]))
