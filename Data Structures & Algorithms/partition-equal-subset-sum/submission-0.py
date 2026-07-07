class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        if total_sum % 2 == 1:
            return False
        target = total_sum / 2
        print(target)
        def recursiveHelper(arr, i, target):
            if i >= len(arr):
                return False
            
            if arr[i] == target:
                return True
            include_output = False
            exclude_output = recursiveHelper(arr, i+1, target)
            if arr[i] < target:
                include_output =  recursiveHelper(arr, i+1, target-arr[i])
            
            return (include_output or exclude_output)
        return recursiveHelper(nums, 0, target)
            


