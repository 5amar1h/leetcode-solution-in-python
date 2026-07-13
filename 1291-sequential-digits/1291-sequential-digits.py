class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        nums = "123456789"
        ans = []

        low_len = len(str(low))
        high_len = len(str(high))

        for length in range(low_len, high_len + 1):
            for start in range(10 - length):
                num = int(nums[start:start + length])
                if low <= num <= high:
                    ans.append(num)

        return ans