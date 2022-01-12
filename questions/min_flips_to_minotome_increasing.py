class Solution:
    def is_monochrome(self, string_under_test):

        last_index_of_zero = string_under_test.rfind("0")
        last_index_of_one = string_under_test.rfind("1")

        if (last_index_of_zero == -1) or (last_index_of_one == -1):
            return True

        if string_under_test[: last_index_of_zero + 1].count("1") > 0:
            return False
        elif (
            string_under_test[last_index_of_zero + 1 : last_index_of_one + 1].count("0")
            > 0
        ):
            return False

        return True

    def minFlipsMonoIncr(self, s: str) -> int:

        one_count, flip_count = 0, 0

        for char in s:

            if char == "1":
                one_count += 1
            else:
                flip_count += 1
            flip_count = min(one_count, flip_count)

        return flip_count


solution = Solution()
print(solution.minFlipsMonoIncr("00110"))
# print(solution.is_monochrome("00111"))
