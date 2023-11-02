def selection_sort(data: list):
    for i in range(len(data)):
        smallest_value = data[i]
        smallest_index = i
        for j in range(i + 1, len(data) - i):
            if data[j] < smallest_value:
                smallest_value = data[j]
                smallest_index = j

        temp = data[i]
        data[i] = smallest_value
        data[smallest_index] = temp

    return data


print(selection_sort([10, 7, 8, 6, 3]))
