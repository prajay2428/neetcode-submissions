class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # min weight will be the max of weights array
        # max weight will be the sum of all the weights of array
        # because if days = 1 then we need to fit all the packages
        # so how to find if a particular weight capacity can meet the 
        # requirement or not 

        def w_works(w):
            summ = 0
            count = 1
            for weight in weights:
                summ += weight
                if summ > w:
                    summ = weight
                    count += 1

            return count <= days

        l = max(weights)
        r = sum(weights)
        while l < r:
            w = (l+r) // 2
            if w_works(w):
                r = w
            else:
                l = w + 1
        return l

