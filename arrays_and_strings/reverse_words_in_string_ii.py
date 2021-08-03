from typing import List


def reverseWords(s: List[str]) -> None:
    temp = []
    word = ""
    for i in range(len(s)):
        if s[i] != " ":
            word = word + s[i]
        else:
            temp.append(word)
            word = ""
    temp.append(word)

    temp.reverse()

    reversed_words = []

    for word in temp:
        for char in word:
            reversed_words.append(char)
        reversed_words.append(" ")

    reversed_words.pop()

    s.clear()

    for char in reversed_words:
        s.append(char)


s = ["t", "h", "e", " ", "s", "k", "y", " ", "i", "s", " ", "b", "l", "u", "e"]
reverseWords(s)
print(s)
