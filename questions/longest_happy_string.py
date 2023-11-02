class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        def can_be_added(string_to_be_checked: str, string_to_be_added: str) -> bool:
            new_string = string_to_be_checked + string_to_be_added

            if "aaa" in new_string:
                return False
            if "bbb" in new_string:
                return False
            if "ccc" in new_string:
                return False

            return True

        letter_list = [("a", a), ("b", b), ("c", c)]
        letter_list = sorted(letter_list, key=lambda x: x[1], reverse=True)

        happy_string = ""
        found = False
        false_counter = 0

        while not found:
            for index, value in enumerate(letter_list):
                if value[1] > 0:
                    if can_be_added(happy_string, value[0]):
                        happy_string = happy_string + value[0]
                        temp_tuple = (value[0], value[1] - 1)
                        letter_list[index] = temp_tuple
                        letter_list = sorted(
                            letter_list, key=lambda x: x[1], reverse=True
                        )
                        false_counter = 0
                        break
                    else:
                        false_counter += 1

            if letter_list[0][1] + letter_list[1][1] + letter_list[2][1] == 0:
                found = True

            if false_counter >= 3:
                found = True

        return happy_string


solution = Solution()

happy_string = solution.longestDiverseString(1, 8, 12)
print(happy_string)
happy_string = solution.longestDiverseString(2, 2, 1)
print(happy_string)
happy_string = solution.longestDiverseString(1, 1, 7)
print(happy_string)
happy_string = solution.longestDiverseString(7, 1, 0)
print(happy_string)
