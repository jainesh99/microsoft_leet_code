from typing import List
from queue import PriorityQueue


class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:

        sorted_box_types = sorted(boxTypes, key=lambda x: x[1], reverse=True)
        maximum_units = 0

        for box_type in sorted_box_types:
            num_of_boxes = box_type[0]
            num_of_units = box_type[1]

            box_count = min(truckSize, num_of_boxes)
            maximum_units = maximum_units + (box_count * num_of_units)
            truckSize -= box_count

            if truckSize <= 0:
                break

        # priority_queue = PriorityQueue()
        # maximum_units = 0
        #
        # for box in boxTypes:
        #     priority_queue.put((-box[1], box[0]))
        #
        # while truckSize != 0:
        #     num_of_units, num_of_boxes = priority_queue.get()
        #     num_of_units = num_of_units * -1
        #     box_count = min(truckSize, num_of_boxes)
        #     maximum_units = maximum_units + (box_count * num_of_units)
        #     truckSize -= box_count

        return maximum_units


solution = Solution()
box_types = [
    [4, 2],
    [5, 5],
    [4, 1],
    [1, 4],
    [2, 5],
    [1, 3],
    [5, 3],
    [1, 5],
    [5, 5],
    [1, 1],
]
truck_size = 24
print(solution.maximumUnits(box_types, truck_size))
