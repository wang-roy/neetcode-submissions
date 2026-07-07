import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        occurrence = {}
        for task in tasks:
            count = occurrence.get(task, 0)
            occurrence.update({task: count+1})
        maxheap = list(occurrence.values())
        heapq.heapify_max(maxheap)
        print(occurrence)
        print(maxheap)

        waitlist = []
        cycle = 0
        while maxheap or waitlist:
            if maxheap:
                count = heapq.heappop_max(maxheap)
                if count - 1 > 0:
                    waitlist.append((cycle, count-1))
            cycle += 1
            while waitlist:
                prevCycle, prevCount = waitlist[0]
                if cycle > prevCycle + n:
                    heapq.heappush_max(maxheap, prevCount)
                    waitlist.pop(0)
                else:
                    break
            print(f"cycle: {cycle}")
            print(maxheap)
            print(waitlist)
        return cycle


