from collections import deque

class Solution(object):
    def maximumSafenessFactor(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)

        # Step 1: Multi-source BFS
        dist = [[-1] * n for _ in xrange(n)]
        q = deque()

        for i in xrange(n):
            for j in xrange(n):
                if grid[i][j] == 1:
                    dist[i][j] = 0
                    q.append((i, j))

        dirs = [(1,0),(-1,0),(0,1),(0,-1)]

        while q:
            x, y = q.popleft()
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and dist[nx][ny] == -1:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))

        # If start or end is a thief
        if dist[0][0] == 0 or dist[n-1][n-1] == 0:
            return 0

        # Check if safeness >= val is possible
        def can(val):
            if dist[0][0] < val:
                return False

            vis = [[False] * n for _ in xrange(n)]
            q = deque([(0, 0)])
            vis[0][0] = True

            while q:
                x, y = q.popleft()
                if x == n - 1 and y == n - 1:
                    return True

                for dx, dy in dirs:
                    nx, ny = x + dx, y + dy
                    if (0 <= nx < n and 0 <= ny < n and
                        not vis[nx][ny] and dist[nx][ny] >= val):
                        vis[nx][ny] = True
                        q.append((nx, ny))

            return False

        lo = 0
        hi = min(dist[0][0], dist[n-1][n-1])

        while lo <= hi:
            mid = (lo + hi) // 2
            if can(mid):
                lo = mid + 1
            else:
                hi = mid - 1

        return hi