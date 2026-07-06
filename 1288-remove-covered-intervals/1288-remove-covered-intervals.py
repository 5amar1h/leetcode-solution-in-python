class Solution(object):
    def removeCoveredIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        # Sort by left ascending, and if equal, right descending
        intervals.sort(key=lambda x: (x[0], -x[1]))

        count = 0
        maxRight = 0

        for l, r in intervals:
            if r > maxRight:
                count += 1
                maxRight = r

        return count