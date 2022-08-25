from typing import List, Dict


def can_construct(target: str, wordbank: List[str], memo: Dict = None):

    if memo is None:
        memo = {}

    if target in memo.keys():
        return memo[target]

    if target == "":
        return True

    for word in wordbank:

        if target.startswith(word):

            if can_construct(target.replace(word, ""), wordbank, memo):
                return True

    memo[target] = False
    return False


print(can_construct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
print(can_construct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
print(can_construct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]))
print(
    can_construct(
        "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",
        ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"],
    )
)
