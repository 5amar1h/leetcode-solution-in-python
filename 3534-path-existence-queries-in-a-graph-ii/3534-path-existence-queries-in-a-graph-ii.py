class Solution(object):
    def pathExistenceQueries(self, n, nums, maxDiff, queries):
        arr = sorted((nums[i], i) for i in range(n))

        pos = [0] * n
        vals = [0] * n
        comp = [0] * n

        for i, (v, idx) in enumerate(arr):
            vals[i] = v
            pos[idx] = i

        cid = 0
        comp[0] = 0
        for i in range(1, n):
            if vals[i] - vals[i - 1] > maxDiff:
                cid += 1
            comp[i] = cid

        nxt = [0] * n
        j = 0
        for i in range(n):
            while j + 1 < n and vals[j + 1] - vals[i] <= maxDiff:
                j += 1
            nxt[i] = j
            if j == i:
                j += 1

        LOG = n.bit_length()
        up = [nxt]
        for _ in range(1, LOG):
            prev = up[-1]
            cur = [0] * n
            for i in range(n):
                cur[i] = prev[prev[i]]
            up.append(cur)

        ans = []

        for u, v in queries:
            if u == v:
                ans.append(0)
                continue

            l = pos[u]
            r = pos[v]
            if l > r:
                l, r = r, l

            if comp[l] != comp[r]:
                ans.append(-1)
                continue

            steps = 0
            cur = l
            for k in range(LOG - 1, -1, -1):
                nx = up[k][cur]
                if nx < r:
                    cur = nx
                    steps += 1 << k

            ans.append(steps + 1)

        return ans