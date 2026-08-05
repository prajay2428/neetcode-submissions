class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        nodes = []
        for i in range(n):
            nodes.append(i)

        g = defaultdict(list)
        for u,v in edges:
            g[u].append(v)
            g[v].append(u)
        

        
        dfs = []
        stack = []
        seen = set()
        count = 0
        
        while len(dfs) != n:
            for node in nodes:
                if node not in dfs:
                    stack.append(node)
                    seen.add(node)
                    break

            count += 1
            while stack:
                node = stack.pop()
                dfs.append(node)
                for nei in g[node]:
                    if nei not in seen:
                        stack.append(nei)
                        seen.add(nei)
        return count

        