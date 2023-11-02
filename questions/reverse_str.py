class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        if len(s) < k:
            return s[::-1]

        if len(s) < (2 * k) and len(s) >= k:
            first_chars = s[0:k]
            return first_chars[::-1] + s[k:]

        return_str = ""

        for i in range(0, len(s), 2 * k):
            word_to_reverse = s[i : i + k]
            return_str = return_str + word_to_reverse[::-1] + s[i + k : i + 2 * k]

        return return_str


solution = Solution()
print(solution.reverseStr("abcdefghijklmno", 3))
