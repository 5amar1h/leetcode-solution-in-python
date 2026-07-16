from fractions import gcd

class Solution(object):
    def gcdSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        arr = []
        mx = 0

        for x in nums:
            if x > mx:
                mx = x
            arr.append(gcd(x, mx))

        arr.sort()

        ans = 0
        n = len(arr)

        for i in range(n // 2):
            ans += gcd(arr[i], arr[n - 1 - i])

        return ans