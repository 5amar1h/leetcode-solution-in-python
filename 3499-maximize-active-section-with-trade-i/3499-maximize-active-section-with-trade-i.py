class Solution(object):
    def maxActiveSectionsAfterTrade(self, s):
        """
        :type s: str
        :rtype: int
        """
        ones = s.count('1')

        t = "1" + s + "1"

        runs = []
        i = 0
        n = len(t)

        while i < n:
            j = i
            while j < n and t[j] == t[i]:
                j += 1
            runs.append((t[i], j - i))
            i = j

        best = 0

        for i in xrange(1, len(runs) - 1):
            if runs[i][0] == '1' and runs[i - 1][0] == '0' and runs[i + 1][0] == '0':
                gain = runs[i - 1][1] + runs[i + 1][1]
                if gain > best:
                    best = gain

        return ones + best