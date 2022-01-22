from typing import List
import heapq


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
intervals = [[13, 15], [1, 13]]
print(solution.minMeetingRooms(intervals))