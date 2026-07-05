class Solution(object):
    def pathsWithMaxScore(self, board):
        MOD = 10 ** 9 + 7
        n = len(board)

        NEG = -1
        score = [[NEG] * n for _ in xrange(n)]
        ways = [[0] * n for _ in xrange(n)]

        score[n - 1][n - 1] = 0
        ways[n - 1][n - 1] = 1

        for i in xrange(n - 1, -1, -1):
            for j in xrange(n - 1, -1, -1):
                if board[i][j] == 'X' or (i == n - 1 and j == n - 1):
                    continue

                best = NEG
                cnt = 0

                for ni, nj in ((i + 1, j), (i, j + 1), (i + 1, j + 1)):
                    if ni < n and nj < n and score[ni][nj] != NEG:
                        if score[ni][nj] > best:
                            best = score[ni][nj]
                            cnt = ways[ni][nj]
                        elif score[ni][nj] == best:
                            cnt = (cnt + ways[ni][nj]) % MOD

                if best == NEG:
                    continue

                val = 0
                if board[i][j] not in ('S', 'E'):
                    val = ord(board[i][j]) - ord('0')

                score[i][j] = best + val
                ways[i][j] = cnt % MOD

        if score[0][0] == NEG:
            return [0, 0]
        return [score[0][0], ways[0][0]]