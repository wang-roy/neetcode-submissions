class Solution:
    def findMin(self, nums: List[int]) -> int:
        def binaryMinSearch(numList):
            print(numList)
            
            mid = (len(numList)-1)//2
            # Case: rotation occurs after this index
            if numList[mid] > numList[-1]:
                return binaryMinSearch(numList[mid+1:])
            # Case: rotation occurs at or before this index
            if numList[mid] < numList[0]:
                return binaryMinSearch(numList[:mid+1])
            # Case: no rotation, numList[0] < numList[mid] < numList[-1] 
            # or degenerate case e.g. length 1 or 2 array
            else:
                return numList[0]
        l = 0
        r = len(nums)-1
        while l < r:
            print(nums[l:r+1])
            mid = (l + r) // 2
            # min is to the right
            if nums[mid] > nums[r]:
                l = mid+1
            # min is to the left
            elif nums[mid] < nums[l]:
                r = mid
            else: 
                return nums[l]
        print(nums[l:r+1])
        return nums[l]
        # return binaryMinSearch(nums)

