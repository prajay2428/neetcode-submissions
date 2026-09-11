class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        print(intervals)
        res = [intervals[0]]

        for current in intervals[1:]:
            if res[-1][1] > current[0]:
                top = res.pop()
                if top[1] > current[1]:
                    res.append(current)
                else:
                    res.append(top)
            
            else:
                res.append(current)
        
        return len(intervals) - len(res)
        