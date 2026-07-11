import heapq
class KthLargest:
    
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.kHeap = []
        for val in nums:
            print(f"considering val {val}")
            if len(self.kHeap) < self.k:
                heapq.heappush(self.kHeap, val)
            elif self.kHeap[0] < val:
                heapq.heapreplace(self.kHeap, val)
            print(f"top of heap {self.kHeap[0]}")
            
        print(f"after init: {self.kHeap}")

    def add(self, val: int) -> int:
        print(f"adding val {val} to heap {self.kHeap}")
        if len(self.kHeap) < self.k:
                heapq.heappush(self.kHeap, val)
        elif self.kHeap[0] < val:
            heapq.heapreplace(self.kHeap, val)

        
        return self.kHeap[0]
        
        
