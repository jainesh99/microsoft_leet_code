from collections import defaultdict, deque
from typing import List


class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:

        ppid_index = defaultdict(list)

        for index, value in enumerate(ppid):

            ppid_index[value].append(index)

        kill_queue = deque(ppid_index[kill])
        response = [kill]

        while kill_queue:

            index_to_kill = kill_queue.popleft()
            response.append(pid[index_to_kill])

            if len(ppid_index[pid[index_to_kill]]) > 0:
                for j in ppid_index[pid[index_to_kill]]:
                    kill_queue.append(j)

        return response


solution = Solution()
pid = [1, 2, 3]
ppid = [0, 1, 2]
kill = 1
solution.killProcess(pid, ppid, kill)
