from typing import List


def count_construct(target: str, word_bank: List[str]) -> int:

    table = [0] * (len(target) + 1)
    table[0] = 1

    for index in range(len(table)):

        for word in word_bank:

            if word == target[index : index + len(word)]:

                table[index + len(word)] += table[index]

    return table[len(target)]


print(count_construct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
print(count_construct("purple", ["purp", "p", "ur", "le", "purpl"]))
print(count_construct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
print(count_construct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]))
print(
    count_construct(
        "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",
        ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"],
    )
)
