"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        interval_list = []
        minHeap = []
        for interval in intervals:
            start = int(interval.start)
            end = int(interval.end)
            interval_list.append([start,end])
            
        
        interval_list.sort()

        for start,end in interval_list:
            if minHeap and start >= minHeap[0]:
                heapq.heappop(minHeap)
            
            heapq.heappush(minHeap,end)
        
        return len(minHeap)
        