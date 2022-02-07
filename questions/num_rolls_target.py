# exmaple
# target = 5, d(dice) = 2, k(faces) = 2
# .    0   1   2   3   4   5
# d0 | 1 | 0 | 0 | 0 | 0 | 0 |
# d1 | 0 | 1 | 1 | 0 | 0 | 0 |
# d2 | 0 | 0 | 1 | 2 | 1 | 0 |
# d3 | 0 | 0 | 0 | 1 | 3 | 3 |

# each value in the table is equal to the all of the combinations of the previous row summed where you can add a dice value and get the new sum

# e.g. you can make 5 with 3 2-sided dice with [2][3] 3(2 ways) + 2 and [2][4] 4(1 way) + 1 or 3 total ways. All values for the previous dice less than target - max face value (or 5 - 3 in this exmaple) can be ignored since it is impossible to produce the target with these values


class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        table = [[0] * (target + 1) for _ in range(n + 1)]
        # can make none with 0 dice 1 way as base case
        table[0][0] = 1

        for dice in range(1, len(table)):
            # can ignore all targets that are less than the number of currently available dice which is why we can start with 'dice'
            for ways in range(dice, len(table[0])):
                table[dice][ways] = sum(
                    [
                        table[dice - 1][validPrevDiceWays]
                        for validPrevDiceWays in range(max(ways - k, 0), ways)
                    ]
                )

        return table[-1][-1] % (10 ** 9 + 7)
