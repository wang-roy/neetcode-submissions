class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        allowance = 0
        for i, jump_len in enumerate(nums):
            allowance = max(jump_len, allowance)
            if allowance == 0 and i < n-1:
                return False
            allowance -= 1
        return True