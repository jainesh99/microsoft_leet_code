import math
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        results = []

        for point in points:

            distance = math.sqrt((point[0]) ** 2 + (point[1]) ** 2)
            results.append((distance, point))

        results.sort()

        k_closest = [results[i][1] for i in range(0, k)]

        return k_closest


solution = Solution()
points = [[1, 3], [-2, 2]]
k = 1
print(solution.kClosest(points, k))

# Alternate Solutions
# class Solution:
#     def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
#         # Since heap is sorted in increasing order,
#         # negate the distance to simulate max heap
#         # and fill the heap with the first k elements of points
#         heap = [(-self.squared_distance(points[i]), i) for i in range(k)]
#         heapq.heapify(heap)
#         for i in range(k, len(points)):
#             dist = -self.squared_distance(points[i])
#             if dist > heap[0][0]:
#                 # If this point is closer than the kth farthest,
#                 # discard the farthest point and add this one
#                 heapq.heappushpop(heap, (dist, i))
#
#         # Return all points stored in the max heap
#         return [points[i] for (_, i) in heap]
#
#     def squared_distance(self, point: List[int]) -> int:
#         """Calculate and return the squared Euclidean distance."""
#         return point[0] ** 2 + point[1] ** 2

# class Solution:
#     def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
#         # Sort the list with a custom comparator function
#         points.sort(key=self.squared_distance)
#
#         # Return the first k elements of the sorted list
#         return points[:k]
#
#     def squared_distance(self, point: List[int]) -> int:
#         """Calculate and return the squared Euclidean distance."""
#         return point[0] ** 2 + point[1] ** 2
