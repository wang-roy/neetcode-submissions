class Solution:
    
    def overlap(self, intA: List[int], intB: List[int]) -> bool:
        if intA[0] < intB[0]:
            return intA[1] >= intB[0]
        elif intA[0] > intB[0]:
            return intB[1] >= intA[0]
        return True

    
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        
        interval = intervals[0]
        if interval[1] < newInterval[0]:
            return [interval] + self.insert(intervals[1:], newInterval)
        
        elif interval[0] > newInterval[1]:
            intervals = [newInterval] + intervals

        else:
        # elif self.overlap(interval, newInterval):
            newInterval[0] = min(interval[0], newInterval[0])
            newInterval[1] = max(interval[1], newInterval[1])
            return self.insert(intervals[1:], newInterval)
        return intervals