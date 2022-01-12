class Solution(object):
    def countBinarySubstrings(self, s: str) -> int:
        index_of_substrings_found = []
        total_binary_substrings = 0
        for i in range(len(s) - 1):
            if s[i] != s[i + 1]:
                index_of_substrings_found.append((i, i + 1))
                total_binary_substrings += 1

        while index_of_substrings_found:
            start, end = index_of_substrings_found.pop()
            if (start - 1 >= 0 and end + 1 < len(s)) and (
                s[start - 1] == s[start] and s[end + 1] == s[end]
            ):
                index_of_substrings_found.append((start - 1, end + 1))
                total_binary_substrings += 1

        return total_binary_substrings


solution = Solution()
solution.countBinarySubstrings("00110011")


"""
So what this solution does is that it starts by first populating the ones with a length of 2 characters i.e in the example
00110011 -> 01, 10, 01

It stores the index of these items in the array i.e -> [(1,2), (3,4), (5,6)] i.e (start, end)

Thereafter it pops one of these sets of indexes, first checks if by subtracting 1 and adding 1 it is still within the bounds of the array

Then checks if the value at start - 1 is = the value at start
Also checks if the value at end + 1 = the value at end

So basically if its 01 at (5,6) then expands it to check if the value at index 4 = value at index 5 and
the value at index 6 = value at index 7

If it is equal then add the new index to the list, and increment the number of total binary strings

This loops until there is no values left.

Another solution but using a streak approach

        ones, zeros, ans = 0, 0, 0

        for i in range(len(s)):
            if s[i] == '0':

                if i > 0 and s[i-1] != '0':
                    zeros = 1
                else:
                    zeros += 1

                if zeros <= ones:
                    ans += 1
            else:

                if i > 0 and s[i - 1] != '1':
                    ones = 1
                else:
                    ones += 1

                if ones <= zeros:
                    ans += 1
        return ans
"""
