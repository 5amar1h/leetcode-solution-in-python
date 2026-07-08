from bisect import bisect_left, bisect_right

class Solution(object):
    def sumAndMultiply(self, s, queries):
        MOD = 10 ** 9 + 7

        pos = []
        digits = []

        for i, ch in enumerate(s):
            if ch != '0':
                pos.append(i)
                digits.append(ord(ch) - ord('0'))

        k = len(digits)

        pow10 = [1] * (k + 1)
        for i in range(1, k + 1):
            pow10[i] = (pow10[i - 1] * 10) % MOD

        prefVal = [0] * (k + 1)
        prefSum = [0] * (k + 1)

        for i in range(k):
            prefVal[i + 1] = (prefVal[i] * 10 + digits[i]) % MOD
            prefSum[i + 1] = prefSum[i] + digits[i]

        ans = []

        for l, r in queries:
            L = bisect_left(pos, l)
            R = bisect_right(pos, r)

            if L == R:
                ans.append(0)
                continue

            length = R - L
            x = (prefVal[R] - prefVal[L] * pow10[length]) % MOD
            sm = prefSum[R] - prefSum[L]

            ans.append((x * sm) % MOD)

        return ans