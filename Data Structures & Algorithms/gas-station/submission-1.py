class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        
        start = 0
        while start < len(gas):
            tank = 0
            j = start
            count = 0
            while count < len(gas):
                tank += gas[j]
                if tank < cost[j]:
                    start = j + 1
                    break
                tank -= cost[j]
                j = (j + 1) % len(gas)
                count += 1
            
            if count == len(gas):
                return start
        
        


        