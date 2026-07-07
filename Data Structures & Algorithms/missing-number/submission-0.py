class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        rangeSum = n * (n + 1)//2
        return rangeSum - sum(nums)