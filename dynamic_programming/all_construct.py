from typing import Dict, List


def all_construct(target: str, word_bank: List[str], memo: Dict = None):

    if memo is None:
        memo = {}

    if target in memo.keys():
        return memo[target]

    if target == "":
        return [[]]

    number_of_ways = []

    for word in word_bank:

        if target.startswith(word):

            value = all_construct(target.removeprefix(word), word_bank)

            if len(value) > 0:
                for item in value:
                    item.insert(0, word)
                    number_of_ways.append(item)

    memo[target] = number_of_ways
    return number_of_ways


print(all_construct("purple", ["purp", "p", "ur", "le", "purpl"]))
print(all_construct("abcdef", ["ab", "abc", "cd", "def", "abcd", "ef", "c"]))
