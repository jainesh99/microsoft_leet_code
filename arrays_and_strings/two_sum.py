from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    hashmap = {}
    for index, value in enumerate(nums):
        difference = target - value

        if difference in hashmap:
            return [index, hashmap[difference]]
        hashmap[value] = index
