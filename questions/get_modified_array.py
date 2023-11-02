from typing import List


class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        # modified_array = [0] * length
        #
        # for update in updates:
        #     start_index = update[0]
        #     end_index = update[1] + 1
        #     modification_value = [update[2]] * (end_index-start_index + 1)
        #
        #     modified_array[start_index:end_index] = [x + y for x, y in zip(modified_array[start_index:end_index], modification_value)]
        #
        # return modified_array

        result = [0] * length

        for update in updates:
            start, end, val = update

            result[start] += val

            if end + 1 < len(result):
                result[end + 1] -= val

        for i in range(1, length):
            result[i] += result[i - 1]

        return result


solution = Solution()
length = 5
updates = [[1, 3, 2], [2, 4, 3], [0, 2, -2]]
print(solution.getModifiedArray(length, updates))
