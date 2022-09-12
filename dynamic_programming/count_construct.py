from typing import Dict, List


def count_construct(target: str, word_bank: List[str], memo: Dict = None):

    if memo is None:
        memo = {}

    if target in memo.keys():
        return memo[target]

    if target == "":
        return 1

    count = 0

    for word in word_bank:

        if target.startswith(word):
            value = count_construct(target.removeprefix(word), word_bank, memo)
            count = count + value

    memo[target] = count
    return count


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
