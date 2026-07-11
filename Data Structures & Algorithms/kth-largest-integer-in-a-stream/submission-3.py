import heapq
class KthLargest:
    
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.kHeap = []
        for val in nums:
            self.kHeapPush(val)
    
    def kHeapPush(self, val: int) -> int:
        if len(self.kHeap) < self.k:
            heapq.heappush(self.kHeap, val)
        elif self.kHeap[0] < val:
            heapq.heapreplace(self.kHeap, val)
        return self.kHeap[0]
    
    def add(self, val: int) -> int:
        return self.kHeapPush(val)
    
    
        
