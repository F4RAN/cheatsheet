from collections import defaultdict, deque
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        indeg = [0] * numCourses

        # b -> a 
        for a, b in prerequisites:
            adj[b].append(a)
            indeg[a] += 1

        q = deque([i for i in range(numCourses) if indeg[i] == 0])
        taken = 0

        while q:
            v = q.popleft()
            taken += 1
            for nb in adj[v]:
                indeg[nb] -= 1
                if indeg[nb] == 0:
                    q.append(nb)

        return taken == numCourses
