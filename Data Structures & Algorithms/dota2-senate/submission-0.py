class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        senate = list(senate)
        n = len(senate)
        R, D = deque(), deque()

        for i, c in enumerate(senate):
            if c == 'R':
                R.append(i)
            else:
                D.append(i)
        

        while R and D:
            r = R.popleft()
            d = D.popleft()
            if r < d:
                R.append(r + n)
            
            else:
                D.append(d + n)
        
        return "Dire" if not R else "Radiant"

        