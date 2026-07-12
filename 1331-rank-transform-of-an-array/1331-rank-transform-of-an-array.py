class Solution(object):
    def arrayRankTransform(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        # Get unique elements and sort them
        unique = sorted(set(arr))

        # Assign ranks
        rank = {}
        r = 1
        for num in unique:
            rank[num] = r
            r += 1

        # Replace each element with its rank
        return [rank[num] for num in arr]