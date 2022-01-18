from typing import List


class Solution:
    def generate_patterns(self,websites: List[str]):

        pattern_list = []

        for i in range(len(websites)-2):
            for j in range(i+1, len(websites)):
                for k in range(j+1, len(websites)):
                    pattern_list.append((websites[i], websites[j], websites[k]))

        return pattern_list

    def mostVisitedPattern(
        self, username: List[str], timestamp: List[int], website: List[str]
    ) -> List[str]:

        users_website_dict = {}
        count_dict = {}

        for index, user in enumerate(username):

            if users_website_dict.get(user):
                temp_arr = users_website_dict[user]
                temp_arr.append(website[index])
            else:
                users_website_dict[user] = [website[index]]

        for user, websites in users_website_dict.items():
            users_website_dict[user] = self.generate_patterns(websites)

        print(users_website_dict)

        for user, patterns in users_website_dict.items():

            for pattern in patterns:

                if not count_dict.get(pattern):
                    count_dict[pattern] = 1

                for compare_user, compare_patterns in users_website_dict.items():

                    if compare_user != user:

                        if pattern in compare_patterns:
                            if count_dict.get(pattern):
                                count_dict[pattern] += 1

                            compare_patterns.remove(pattern)

        results = {}

        for pattern, value in count_dict.items():

            if results.get(value):
                results[value].append(pattern)
            else:
                results[value] = [pattern]

        print(results)

        sorted_results = results[sorted(results, reverse=True)[0]]

        if len(sorted_results) > 1:
            return list(sorted(sorted_results)[0])
        else:
            return list(sorted_results[0])


username = ["joe","joe","joe","james","james","james","james","mary","mary","mary"]
timestamp = [1,2,3,4,5,6,7,8,9,10]
website = ["home","about","career","home","cart","maps","home","home","about","career"]

solution = Solution()
print(solution.mostVisitedPattern(username, timestamp, website))



