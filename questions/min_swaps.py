from typing import List


class Solution:
    def minSwaps(self, data: List[int]) -> int:

        number_of_ones = data.count(1)

        if number_of_ones == 1:
            return 0

        # min_swaps = float("inf")

        # for i in range(len(data)):
        #     window = data[i:i+number_of_ones]
        #
        #     if len(window) == number_of_ones:
        #         swaps_needed = window.count(0)
        #
        #         if swaps_needed <= min_swaps:
        #             min_swaps = swaps_needed

        window = []
        number_of_ones_in_window = 0
        max_number_of_ones_in_window = 0

        for num in data:
            window.append(num)
            number_of_ones_in_window += num

            if len(window) == number_of_ones:

                if number_of_ones_in_window > max_number_of_ones_in_window:
                    max_number_of_ones_in_window = number_of_ones_in_window

                number_of_ones_in_window = number_of_ones_in_window - window.pop(0)

        return number_of_ones - max_number_of_ones_in_window


solution = Solution()
data = [1, 0, 1, 0, 1]
print(solution.minSwaps(data))
