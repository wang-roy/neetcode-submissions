class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        L = [1] * n
        LIS = -1
        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                if nums[i] < nums[j]:
                      L[i] = max(L[i], L[j] + 1)
            if LIS < L[i]:
                LIS = L[i]
            # print(L)
        
        return LIS