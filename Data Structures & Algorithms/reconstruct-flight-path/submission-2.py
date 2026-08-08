class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        tickets.sort()

        g = defaultdict(list)

        for src, dst in tickets:
            g[src].append(dst)

        res = []

        def dfs(src):
            while g[src]:
                dst = g[src].pop(0)
                dfs(dst)

            res.append(src)

        dfs("JFK")

        return res[::-1]