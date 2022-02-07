from typing import List


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        def generate_dict(word: str):
            result_dictionary = {}

            for char in word:

                if char in result_dictionary.keys():
                    result_dictionary[char] += 1
                else:
                    result_dictionary[char] = 1

            return result_dictionary

        char_dict = generate_dict(chars)
        counter = 0
        for word in words:

            word_dict = generate_dict(word)
            word_list = [char for char in word]
            for key in word_dict.keys():
                if key in char_dict.keys():

                    if word_dict[key] <= char_dict[key]:
                        for i in range(0, word_dict[key]):
                            word_list.remove(key)
                else:
                    break

            if len(word_list) == 0:
                counter = counter + len(word)

        return counter


solution = Solution()
words = ["hello", "world", "leetcode"]
chars = "welldonehoneyr"
print(solution.countCharacters(words, chars))
