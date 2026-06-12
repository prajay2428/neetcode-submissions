class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0]*len(temperatures)

        # brute force approach

        for i in range(len(temperatures)):
            for j in range(i+1,len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    result[i] = j-i
                    break
                
            

        return result
                

        