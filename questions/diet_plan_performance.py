from typing import List


class Solution:
    def dietPlanPerformance(
        self, calories: List[int], k: int, lower: int, upper: int
    ) -> int:
        performance = 0
        # Brute Force
        # if k == 1:
        #     for calorie in calories:
        #         if calorie < lower:
        #             performance -= 1
        #         elif calorie > upper:
        #             performance += 1
        # elif k > 1:
        #     for i in range(0, len(calories)):
        #         calories_to_count = calories[i:i+k]
        #
        #         if len(calories_to_count) == k:
        #             max_calories = max(calories_to_count)
        #
        #             if max_calories>upper:
        #                 performance += 1
        #             else:
        #                 sum_calories = sum(calories_to_count)
        #                 if sum_calories < lower:
        #                     performance -= 1
        #                 elif sum_calories > upper:
        #                     performance += 1
        #
        # return performance

        # Sliding window
        window = []
        sum_so_far = 0

        for calorie in calories:
            window.append(calorie)
            sum_so_far += calorie

            if len(window) == k:
                if sum_so_far > upper:
                    performance += 1
                elif sum_so_far < lower:
                    performance -= 1

                beginning_of_window = window.pop(0)
                sum_so_far -= beginning_of_window

        return performance


solution = Solution()

calories = [3, 2]
k = 2
lower = 0
upper = 1

print(solution.dietPlanPerformance(calories, k, lower, upper))
