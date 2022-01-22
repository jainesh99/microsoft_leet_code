class Solution:
    def isValid(self, s: str) -> bool:
        openings = "([{"
        closing = ")]}"
        pairs = {"(": ")", "[": "]", "{": "}"}
        test_str = []
        opening_count = 0
        closing_count = 0

        if len(s) == 1:
            return False

        for char in s:
            if char in openings:
                opening_count += 1
                test_str.append(char)
            if char in closing:
                closing_count += 1

                if test_str:
                    if char != pairs[test_str[len(test_str) - 1]]:
                        return False
                    test_str.pop()
                else:
                    return False

        if opening_count != closing_count:
            return False

        return True
