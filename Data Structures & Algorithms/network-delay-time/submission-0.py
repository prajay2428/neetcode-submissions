import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        g = defaultdict(list)
        for u,v,time in times:
            g[u].append((v,time))
        
        min_heights = {}
        min_heap = [(0,k)] # { time it takes to reach node from source, node}

        while min_heap:
            time_k_to_i, i = heapq.heappop(min_heap)
            if i in min_heights:
                continue
            min_heights[i] = time_k_to_i

            for nei,time in g[i]:
                if nei not in min_heights:
                    heapq.heappush(min_heap,(time_k_to_i + time, nei))
        
        if len(min_heights) != n:
            return -1
        
        return max(min_heights.values())


            

        
        