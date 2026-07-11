class Solution:


    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        newList = []
        i = 0
        n = len(intervals)
        # append non overlapping intervals with end values smaller than the new interval's start value
        while i < n and intervals[i][1] < newInterval[0]:
            newList.append(intervals[i])
            i += 1
        
        while i < len(intervals) and newInterval[1] >= intervals[i][0]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        
        newList.append(newInterval)

        while i < n: 
            newList.append(intervals[i])
            i += 1


        return newList