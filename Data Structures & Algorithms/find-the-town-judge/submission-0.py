class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        incoming = {}
        outgoing = {}
        for i in range(1,n+1):
            incoming[i] = 0
            outgoing[i] = 0
        
        for u,v in trust:
            outgoing[u] += 1
            incoming[v] += 1

        
        for i in range(1,n+1):
            if incoming[i] == n-1 and outgoing[i] ==0:
                return i
        
        return -1
        