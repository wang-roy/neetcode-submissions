import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        heap = []
        
        for i, num in enumerate(nums):
            heapq.heappush(heap, (-1*num, i))
            while heap[0][1] < i - k + 1:
                heapq.heappop(heap)
            result.append(-1*heap[0][0])
        
        return result[k-1:]
