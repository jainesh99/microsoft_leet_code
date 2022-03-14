from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagram_groups = defaultdict(list)

        for anagram_str in strs:
            anagram_groups["".join(sorted(anagram_str))].append(anagram_str)

        return [value for key, value in anagram_groups.items()]


solution = Solution()
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(solution.groupAnagrams(strs))
