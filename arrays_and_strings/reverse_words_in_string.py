def reverseWords(s: str):
    s = s.strip()
    s = s.split(" ")
    reverse_str = ""
    for i in range(len(s) - 1, -1, -1):
        if len(s[i]) > 0:
            reverse_str = reverse_str + s[i] + " "

    return reverse_str.strip()


# print(reverseWords("the sky is blue"))
print(reverseWords("  hello world  "))
print(reverseWords("a good   example"))
print(reverseWords("  Bob    Loves  Alice   "))
print(reverseWords("Alice does not even like bob"))
