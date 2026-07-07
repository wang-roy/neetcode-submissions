class Solution:
    def findMin(self, nums: List[int]) -> int:
        def binaryMinSearch(numList):
            print(numList)
            if len(numList) == 1:
                return numList[0]
            elif len(numList) == 2:
                return min(numList[0], numList[1])
            
            mid = len(numList)//2
            # Case: rotation occurs after this index
            if numList[mid] > numList[-1]:
                return binaryMinSearch(numList[mid+1:])
            # Case: rotation occurs at or before this index
            if numList[mid] < numList[0]:
                return binaryMinSearch(numList[:mid+1])
            # Case: no rotation (numList[0] < numList[mid] < numList[-1])
            else:
                return numList[0]
        return binaryMinSearch(nums)
            
                

