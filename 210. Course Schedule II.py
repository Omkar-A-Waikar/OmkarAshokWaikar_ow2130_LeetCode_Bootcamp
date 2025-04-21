from collections import deque
from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequeuisites: List[List[int]]) -> List[int]:
        adjacent = [[] for _ in range(numCourses)]
        iDeg = [0] * numCourses
        
        for course, pre in prerequeuisites:
            adjacent[pre].append(course)
            iDeg[course] += 1
        
        que = deque([i for i in range(numCourses) if iDeg[i] == 0])
        op = []
        
        while que:
            node = que.popleft()
            op.append(node)
            
            for n1 in adjacent[node]:
                iDeg[n1] -= 1
                if iDeg[n1] == 0:
                    que.append(n1)
        
        return op if len(op) == numCourses else []
