def longestPalindrome(s: str) -> str:
    longest_palindrome = ""
    increment = 2

    if s == s[::-1]:
        return s

    if len(s) == 2:
        if s[0] == s[1]:
            return s

    for x in range(0, len(s)):
        for y in range(x + increment, len(s) + 1):
            cut_string = s[x:y]
            reverse_string = cut_string[::-1]

            if cut_string == reverse_string and len(cut_string) > len(
                longest_palindrome
            ):
                longest_palindrome = cut_string
                increment = len(longest_palindrome)

    if not longest_palindrome:
        return s[0]

    return longest_palindrome
