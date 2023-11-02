from typing import List, NamedTuple


class IndexHeight(NamedTuple):
    index: int
    height: int


class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        water = 0
        for index, bar_height in enumerate(height):
            # we need to see if we can form a container
            while stack and bar_height >= stack[-1][0]:
                popped, _ = stack.pop()
                # is it a container though? we have a left border?
                if stack:
                    left_border, j = stack[-1]
                    # we compute the water
                    water += min(left_border - popped, bar_height - popped) * (
                        index - j - 1
                    )
            stack.append((bar_height, index))
        return water


solution = Solution()
solution.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])

"""
Basically you are adding the items to the stack, once you find an item which is greater than the top of the stack
You the pop it, and by doing so you skip an element to go further back where the actual left border is
From there you calculate how much is left
"""
