class Solution:
    def getSum(self, a: int, b: int) -> int:
        bit_shortener = 0xFFFFFFFF

        while (b & bit_shortener) > 0:
            carry = (a & b) << 1
            a = a ^ b
            b = carry

        return (a & bit_shortener) if b > 0 else a


solution = Solution()
solution.getSum(1, 2)
