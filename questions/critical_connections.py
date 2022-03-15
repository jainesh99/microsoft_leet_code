import collections
from typing import List


class Solution:
    def criticalConnections(
        self, n: int, connections: List[List[int]]
    ) -> List[List[int]]:
        graph = collections.defaultdict(list)

        for i, j in connections:
            graph[i].append(j)
            graph[j].append(i)

        low = [0] * n

        visited = set()

        res = []

        def dfs(node, parent, timer):

            nonlocal low, graph, res, visited

            low[node] = timer

            visited.add(node)

            for child in graph[node]:

                if child == parent:
                    continue
                if child not in visited:
                    dfs(child, node, timer + 1)  # Probably can be done with a stack!

                low[node] = min(low[node], low[child])

                # important condition

                # this will check all the node which are reachable from the this node having time greater than the parent if less then it will be access from somewhere else
                # in teh minimum time

                if timer < low[child]:
                    res.append([node, child])

        dfs(0, -1, 0)
        return res


solution = Solution()
print(solution.criticalConnections(4, [[0, 1], [1, 2], [2, 0], [1, 3]]))
# print(solution.criticalConnections(6, [[0, 1], [1, 2], [2, 0], [1, 3], [3, 4], [4, 5], [5, 3]]))
