class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        output = ""

        if str1 == str2:
            return str1

        if len(str1) > len(str2):
            chosen_str = str2
            string_to_match = str1
        else:
            chosen_str = str1
            string_to_match = str2

        for i in range(1, len(chosen_str) + 1):
            string_to_test = chosen_str[:i] * (len(string_to_match) // i)

            if string_to_test == string_to_match:
                if len(chosen_str[:i]) > len(output):
                    if str1.count(chosen_str[:i]) * len(chosen_str[:i]) == len(
                        str1
                    ) and str2.count(chosen_str[:i]) * len(chosen_str[:i]) == len(str2):
                        output = chosen_str[:i]

        return output


solution = Solution()
# str1 = "ABABABAB"
# str2 = "ABAB"
# str1 = "TAUXXTAUXXTAUXXTAUXXTAUXX"
# str2 = "TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX"
# str1 = "AAAAAAAAA"
# str2 = "AAACCC"
str1 = "ABCABC"
str2 = "ABC"
print(solution.gcdOfStrings(str1, str2))
