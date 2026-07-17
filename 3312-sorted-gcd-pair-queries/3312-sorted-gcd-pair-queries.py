from bisect import bisect_right

class Solution(object):
    def gcdValues(self, nums, queries):
        mx = max(nums)

        freq = [0] * (mx + 1)
        for x in nums:
            freq[x] += 1

        cnt = [0] * (mx + 1)

        for d in xrange(1, mx + 1):
            s = 0
            for m in xrange(d, mx + 1, d):
                s += freq[m]
            cnt[d] = s

        exact = [0] * (mx + 1)

        for d in xrange(mx, 0, -1):
            c = cnt[d]
            val = c * (c - 1) // 2
            for m in xrange(d + d, mx + 1, d):
                val -= exact[m]
            exact[d] = val

        pref = [0] * (mx + 1)
        cur = 0
        for d in xrange(1, mx + 1):
            cur += exact[d]
            pref[d] = cur

        ans = []
        for q in queries:
            ans.append(bisect_right(pref, q))

        return ans