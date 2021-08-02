from typing import List


def reverseString(s: List[str]) -> None:
    start_pointer = 0
    end_pointer = len(s)-1

    while start_pointer < end_pointer:
        print(f"Start Pointer {start_pointer} and End Pointer {end_pointer}")
        temp = s[start_pointer]

        s[start_pointer] = s[end_pointer]
        s[end_pointer] = temp

        start_pointer += 1
        end_pointer -= 1

    for i in range(len(s)):
        if i < (len(s) - i - 1):
            temp = s[i]

            s[i] = s[len(s) - i - 1]
            s[len(s) - i - 1] = temp


test = ["H", "a", "n", "n", "a", "h"]
reverseString(test)
print(test)
