import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance(x1, x2):
            x_dist = math.pow(x1[0] - x2[0], 2)
            y_dist = math.pow(x1[1] - x2[1], 2)
            return math.pow(math.sqrt(x_dist + y_dist), 2)
        maxHeap = []

        for point in points:
            dist = distance(point, [0, 0])
            print(dist)
            if len(maxHeap) >= k:
                if dist < maxHeap[0][0]:
                    heapq.heappop_max(maxHeap)
                else:
                    continue
            heapq.heappush_max(maxHeap, (dist, point))
            print(maxHeap)
        return [point for _, point in maxHeap]


                
            
