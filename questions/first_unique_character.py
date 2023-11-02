from collections import Counter, defaultdict


class Solution:
    def firstUniqChar(self, s: str) -> int:
        # if len(s) == 1:
        #     return 0
        #
        # index_dict = defaultdict(list)
        #
        # for index, char in enumerate(s):
        #
        #     index_dict[char].append(index)
        #
        # single_occurrence = [
        #     (index[0], character)
        #     for character, index in index_dict.items()
        #     if len(index) == 1
        # ]
        #
        # if single_occurrence:
        #     return single_occurrence[0][0]
        # else:
        #     return -1

        # build hash map : character and how often it appears
        count = Counter(s)

        # find the index
        for idx, ch in enumerate(s):
            if count[ch] == 1:
                return idx
        return -1


solution = Solution()
s = "leetcode"
print(solution.firstUniqChar(s))
