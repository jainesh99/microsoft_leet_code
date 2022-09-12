from copy import deepcopy
from typing import List


def all_construct(target: str, word_bank: List[str]) -> List[List[str]]:

    table = [[] for x in range(len(target) + 1)]
    table[0] = [[]]

    for index in range(len(table)):

        for word in word_bank:

            if word == target[index : index + len(word)]:

                for item in table[index]:

                    temp = deepcopy(item)
                    temp.append(word)
                    table[index + len(word)].append(temp)

    return table[len(target)]


print(all_construct("abcdef", ["ab", "abc", "cd", "def", "abcd", "ef", "c"]))
print(all_construct("purple", ["purp", "p", "ur", "le", "purpl"]))
print(all_construct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
