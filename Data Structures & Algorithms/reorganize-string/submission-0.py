from collections import Counter
import heapq


class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)

        max_heap = [(-freq, ch) for ch, freq in count.items()]
        heapq.heapify(max_heap)

        prev_count = 0
        prev_char = ""
        result = []

        while max_heap:
            count, ch = heapq.heappop(max_heap)

            result.append(ch)
            count += 1  # Negative count moves toward zero

            if prev_count < 0:
                heapq.heappush(max_heap, (prev_count, prev_char))

            prev_count = count
            prev_char = ch

        if prev_count < 0:
            return ""

        return "".join(result)