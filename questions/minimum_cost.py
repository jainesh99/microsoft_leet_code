from typing import List
import heapq


class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        # build graph
        graph = {}
        for i in range(1, n + 1):
            graph[i] = []
        for x, y, cost in connections:
            graph[x].append((y, cost))
            graph[y].append((x, cost))

        # dijkstra
        pq = [(0, 1)]
        visited = set()
        total = 0
        while pq:
            cost, node = heapq.heappop(pq)
            if node in visited:
                continue
            visited.add(node)
            total += cost
            for neighbor, neighbor_cost in graph[node]:
                if neighbor not in visited:
                    heapq.heappush(pq, (neighbor_cost, neighbor))
        return total if len(visited) == n else -1
