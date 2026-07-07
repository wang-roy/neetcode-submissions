class Solution:
    def findMin(self, nums: List[int]) -> int:
        def binaryMinSearch(numList):
            print(numList)
            if len(numList) == 1:
                return numList[0]
            elif len(numList) == 2:
                return min(numList[0], numList[1])
            
            mid = len(numList)//2
            if numList[mid] > numList[-1]:
                return binaryMinSearch(numList[mid+1:])
            if numList[mid] < numList[0]:
                return binaryMinSearch(numList[:mid+1])
            else:
                return binaryMinSearch(numList[:mid])
        return binaryMinSearch(nums)
            
                

