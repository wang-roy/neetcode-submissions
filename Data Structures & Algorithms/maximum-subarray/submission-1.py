class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # iterate through array and keep track of running sum + max sum 
        # if running sum ever < 0, it's worse to stay with previous numbers than starting at 0 from next index 

        maxSum = -1 * sys.maxsize - 1
        runningSum = 0
        for num in nums:
            runningSum += num
            if maxSum < runningSum:
                maxSum = runningSum
            if runningSum < 0:
                runningSum = 0
        
        return maxSum
