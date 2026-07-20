class Solution(object):
    def shiftGrid(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        m = len(grid)
        n = len(grid[0])
        total = m * n

        k %= total

        ans = [[0] * n for _ in xrange(m)]

        for i in xrange(m):
            for j in xrange(n):
                old = i * n + j
                new = (old + k) % total
                r = new // n
                c = new % n
                ans[r][c] = grid[i][j]

        return ans