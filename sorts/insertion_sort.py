def insertion_sort(data: list):

    for i in range(1, len(data)):
        value_to_compare = data[i]

        for j in range(i - 1, -1, -1):

            if data[j] < value_to_compare:
                break
            else:
                data[j + 1] = data[j]
            data[j] = value_to_compare

    return data


print(insertion_sort([7, 8, 6, 3, 9]))
