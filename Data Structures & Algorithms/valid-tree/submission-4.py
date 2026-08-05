class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        stack = [0]
        seen = set()

        while stack:
            node = stack.pop()

            if node in seen:
                continue

            seen.add(node)

            for neighbour in graph[node]:
                if neighbour not in seen:
                    stack.append(neighbour)

        return len(seen) == n