class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        if len(s) == 1:
            return 1

        max_length = 0
        unique = {}
        substring = ""
        index = 0

        while index != len(s):
            if unique.get(s[index]) is None:
                unique[s[index]] = index
                substring = substring + s[index]
                index += 1
            else:
                if len(substring) > max_length:
                    max_length = len(substring)

                first_index_of_duplicate = unique[s[index]]
                index = first_index_of_duplicate + 1
                substring = ""
                unique = {}

        return len(substring) if len(substring) > max_length else max_length


solution = Solution()
print(solution.lengthOfLongestSubstring("abba"))
