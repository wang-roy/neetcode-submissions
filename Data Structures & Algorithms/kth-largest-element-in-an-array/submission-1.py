import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        kHeap = []
        for num in nums:
            if len(kHeap) < k:
                heapq.heappush(kHeap, num)
            elif len(kHeap) == k and num > kHeap[0]:
                heapq.heapreplace(kHeap, num)
        return kHeap[0]