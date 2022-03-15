import itertools
from typing import List

# class Solution:
#     def generate_patterns(self,websites: List[str]):
#
#         pattern_list = []
#
#         for i in range(len(websites)-2):
#             for j in range(i+1, len(websites)):
#                 for k in range(j+1, len(websites)):
#                     pattern_list.append((websites[i], websites[j], websites[k]))
#
#         return pattern_list
#
#     def mostVisitedPattern(
#         self, username: List[str], timestamp: List[int], website: List[str]
#     ) -> List[str]:
#
#         users_website_dict = {}
#         count_dict = {}
#
#         logs_tuple = sorted(zip(username, timestamp, website))
#
#         for user, time, web in logs_tuple:
#
#             if users_website_dict.get(user):
#                 temp_arr = users_website_dict[user]
#                 temp_arr.append(web)
#             else:
#                 users_website_dict[user] = [web]
#
#         for user, websites in users_website_dict.items():
#             users_website_dict[user] = self.generate_patterns(websites)
#
#         print(users_website_dict)
#
#         for user, patterns in users_website_dict.items():
#
#             for pattern in patterns:
#
#                 if not count_dict.get(pattern):
#                     count_dict[pattern] = 1
#
#                 for compare_user, compare_patterns in users_website_dict.items():
#
#                     if compare_user != user:
#
#                         if pattern in compare_patterns:
#                             if count_dict.get(pattern):
#                                 count_dict[pattern] += 1
#
#                             compare_patterns.remove(pattern)
#
#         results = {}
#
#         for pattern, value in count_dict.items():
#
#             if results.get(value):
#                 results[value].append(pattern)
#             else:
#                 results[value] = [pattern]
#
#         print(results)
#
#         sorted_results = results[sorted(results, reverse=True)[0]]
#
#         if len(sorted_results) > 1:
#             return list(sorted(sorted_results)[0])
#         else:
#             return list(sorted_results[0])


class Solution:
    def mostVisitedPattern(
        self, username: List[str], timestamp: List[int], website: List[str]
    ) -> List[str]:

        graph = {}

        logs_tuple = sorted(zip(username, timestamp, website))

        for user, time, website_visited in logs_tuple:
            if user not in graph:
                graph[user] = [website_visited]
            else:
                graph[user].append(website_visited)

        counter = {}

        for user, website_visited in graph.items():
            # here we are creating any possible combinations of websites --of length 3- aa,bb,cc or bb,cc,dd etc
            all_website_patterns = set(itertools.combinations(website_visited, 3))
            for triple in all_website_patterns:
                if triple in counter:
                    counter[triple] += 1
                else:
                    counter[triple] = 1

        sorted_tuples = sorted(counter.items(), key=lambda item: item[1], reverse=True)
        results = {}

        for pattern, value in sorted_tuples:

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


username = [
    "joe",
    "joe",
    "joe",
    "james",
    "james",
    "james",
    "james",
    "mary",
    "mary",
    "mary",
]
timestamp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
website = [
    "home",
    "about",
    "career",
    "home",
    "cart",
    "maps",
    "home",
    "home",
    "about",
    "career",
]

# username = ["dowg","dowg","dowg"]
# timestamp = [158931262,562600350,148438945]
# website = ["y","loedo","y"]

solution = Solution()
print(solution.mostVisitedPattern(username, timestamp, website))
