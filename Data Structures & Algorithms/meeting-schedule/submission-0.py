"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        interval_list = []
        for interval in intervals:
            start = int(interval.start)
            end = int(interval.end)
            interval_list.append([start,end])
        
        interval_list.sort()

        for i in range(1,len(interval_list)):
            if interval_list[i][0] < interval_list[i-1][1]:
                return False
            
        return True

