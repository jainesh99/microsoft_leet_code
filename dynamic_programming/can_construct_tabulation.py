from collections import defaultdict
from typing import List


def can_construct(target: str, word_bank: List[str]) -> bool:

    table = [False] * (len(target) + 1)
    table[0] = True

    for index, letter in enumerate(target):

        if table[index]:

            for word in word_bank:

                if target[index : index + len(word)] == word:
                    table[index + len(word)] = True

    return table[len(target)]


print(can_construct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
print(can_construct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
print(can_construct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]))
print(
    can_construct(
        "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",
        ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"],
    )
)
