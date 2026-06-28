class Solution(object):
    def maximumElementAfterDecrementingAndRearranging(self, arr):
        arr.sort()
        arr[0] = 1

        for i in xrange(1, len(arr)):
            if arr[i] > arr[i - 1] + 1:
                arr[i] = arr[i - 1] + 1

        return arr[-1]