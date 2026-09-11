class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = [intervals[0]]
        print(res)

        for current in intervals[1:]:
            if res[-1][1] >= current[0]:
                res[-1][1] = max(current[1],res[-1][1])
            else:
                res.append(current)
        
        return res
        