from typing import List


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:

        digit_logs = []
        letter_logs = []

        for log in logs:
            if log.split(" ")[1].isdigit():
                digit_logs.append(log)
            else:
                identifier, log_value = log.split(" ", 1)
                letter_logs.append((log_value, identifier))

        sorted_letter_logs = sorted(letter_logs)

        sorted_logs = [log[1] + " " + log[0] for log in sorted_letter_logs]

        for log in digit_logs:
            sorted_logs.append(log)

        return sorted_logs


solution = Solution()

logs = ["a1 9 2 3 1", "g1 act car", "zo4 4 7", "ab1 off key dog", "a8 act zoo"]

print(solution.reorderLogFiles(logs))
