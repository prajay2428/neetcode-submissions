class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        g = defaultdict(list)
        for u,v in edges:
            g[u].append(v)
            g[v].append(u)
        print(g)
        min_heights = []
        min_height = float('inf')
        
        # for every node, take that node as starting node and perform dfs
        for i in range(n):
            stack = [(i,0)]
            seen = {i}
            height = 0
            while stack:
                node,depth = stack.pop()
                height = max(height,depth)
                for nei in g[node]:
                    if nei not in seen:
                        seen.add(nei)
                        stack.append((nei,depth+1))
            
            min_heights.append((i,height))
        
        print(min_heights)

        for node,height in min_heights:
            min_height = min(height,min_height)

        result = []

        for node,height in min_heights:
            if height == min_height:
                result.append(node)
        
        return result

        
