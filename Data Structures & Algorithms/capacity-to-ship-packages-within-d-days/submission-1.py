class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        def w_works(w):
            summ = 0
            days_used = 1
            for weight in weights:
                summ += weight
                if summ > w:
                    summ = weight
                    days_used += 1

            return days_used <= days

        l = max(weights)
        r = sum(weights)
        while l < r:
            w = (l+r) // 2
            if w_works(w):
                r = w
            else:
                l = w + 1
        return l

