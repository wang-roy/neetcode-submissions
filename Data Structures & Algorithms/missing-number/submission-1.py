class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        # n = len(nums)
        # rangeSum = n * (n + 1)//2
        # return rangeSum - sum(nums)
        n = len(nums)
        result = n
        for i in range(0, n):
            result ^= i
        
        for num in nums:
            result ^= num
        
        return result