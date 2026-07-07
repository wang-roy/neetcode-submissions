import heapq
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        swap_endpoints = [(end, start) for (start, end) in intervals]
        print(swap_endpoints)

        heapq.heapify(swap_endpoints)
        reverseInterval = heapq.heappop(swap_endpoints)
        nonOverlapEnd = reverseInterval[0]
        nonOverlapStart = reverseInterval[1]
        eraseCount = 0
        while len(swap_endpoints) > 0:
            reverseIntervalEnd, reverseIntervalStart = heapq.heappop(swap_endpoints)
            if reverseIntervalStart >= nonOverlapEnd:
                nonOverlapEnd = reverseIntervalEnd
            else:
                print(f"interval removed: ({reverseIntervalStart}, {reverseIntervalEnd})")
                eraseCount += 1
        return eraseCount
