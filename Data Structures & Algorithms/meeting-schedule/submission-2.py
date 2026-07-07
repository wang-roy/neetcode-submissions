"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        n = len(intervals)
        sorted_intervals = sorted([(interval.start, interval.end) for interval in intervals])
        if sorted_intervals:
            prev_end = sorted_intervals[0][1]
            for i in range(1, n):
                curr_start = sorted_intervals[i][0]
                if prev_end > curr_start:
                    return False
                prev_end = sorted_intervals[i][1]
        
        return True
        
