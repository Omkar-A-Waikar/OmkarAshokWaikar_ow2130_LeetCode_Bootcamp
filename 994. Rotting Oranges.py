from collections import deque

class Solution(object):
    def orangesRotting(self, grid):
        m, n = len(grid), len(grid[0])
        q = deque()
        notVisited = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i, j))
                elif grid[i][j] == 1:
                    notVisited += 1
        
        if notVisited == 0:
            return 0
        
        direction = [(1,0), (-1,0), (0,1), (0,-1)]
        time = 0
        
        while q and notVisited > 0:
            for _ in range(len(q)):
                x, y = q.popleft()
                for dx, dy in direction:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                        grid[nx][ny] = 2    
                        notVisited -= 1  
                        q.append((nx, ny))
            time += 1
        
        return time if notVisited == 0 else -1
