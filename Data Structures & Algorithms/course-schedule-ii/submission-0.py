class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        VISITING = 1
        UNVISITED = 0
        VISITED = 2
        ans = []
        g = defaultdict(list)
        courses = prerequisites
        states = [UNVISITED]*numCourses

        for a,b in courses:
            g[a].append(b)
        
        def dfs(node):
            state = states[node]
            if state == VISITED:
                return True
            elif state == VISITING:
                return False
            
            states[node] = VISITING

            for nei in g[node]:
                if not dfs(nei):
                    return False
                
            states[node] = VISITED
            ans.append(node)
            return True

            
        

        for i in range(numCourses):
            if not dfs(i):
                return []
        
        return ans

        