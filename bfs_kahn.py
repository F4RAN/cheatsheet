from collections import defaultdict, deque
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list) # Dictionary which each key by default has array value
        indeg = [0] * numCourses # Suppose all courses don't need any prerequisites

        # b -> a 
        for a, b in prerequisites:
            adj[b].append(a)
            indeg[a] += 1 # before passing a we should passed b

        q = deque([i for i in range(numCourses) if indeg[i] == 0]) # all courses which don't have any prerequisites can be selected at first
        taken = 0

        while q:
            v = q.popleft() # from left pick course
            taken += 1 # pass
            for nb in adj[v]: # update prerequisites of others (find in neighbors)
                indeg[nb] -= 1 # One of prerequisites passed
                if indeg[nb] == 0: # no prerequisites anymore so we can pass it
                    q.append(nb)

        return taken == numCourses # Can we pass all courses

        """
        If q be empty and taken != numCourses it means we have some courses
        which we can not pass them because they still have prerequisites
        """
