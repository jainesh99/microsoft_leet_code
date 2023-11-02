from collections import defaultdict
from typing import List


class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        counter_dict = defaultdict(lambda: 0)

        for value in arr:
            counter_dict[value] = counter_dict[value] + 1

        if k == 0:
            return len(counter_dict)

        counter_tuple = sorted(
            counter_dict.items(), key=lambda item: item[1], reverse=True
        )

        while k > 0:
            item, count = counter_tuple.pop()

            if count > k:
                counter_tuple.append((item, count - k))
                k = 0
            elif count <= k:
                k = k - count

        return len(counter_tuple)


solution = Solution()
arr = [4, 3, 1, 1, 3, 3, 2]
k = 3
print(solution.findLeastNumOfUniqueInts(arr, k))
