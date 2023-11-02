import heapq
from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])

        rooms = []

        heapq.heappush(rooms, intervals[0][1])

        for interval in intervals[1:]:
            if interval[0] >= rooms[0]:
                heapq.heappop(rooms)
                heapq.heappush(rooms, interval[1])
            else:
                heapq.heappush(rooms, interval[1])

        return len(rooms)


solution = Solution()
intervals = [[0, 30], [5, 10], [15, 20]]
print(solution.minMeetingRooms(intervals))
