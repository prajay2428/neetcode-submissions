import heapq


class MedianFinder:

    def __init__(self):
        # Max heap for the smaller half.
        # Python only has a min heap, so store values as negatives.
        self.smallHeap = []

        # Min heap for the larger half.
        self.bigHeap = []

    def addNum(self, num: int) -> None:
        # Put the number into the appropriate heap.
        if not self.smallHeap or num <= -self.smallHeap[0]:
            heapq.heappush(self.smallHeap, -num)
        else:
            heapq.heappush(self.bigHeap, num)

        # Balance the heaps so their sizes differ by at most 1.
        if len(self.smallHeap) > len(self.bigHeap) + 1:
            value = -heapq.heappop(self.smallHeap)
            heapq.heappush(self.bigHeap, value)

        elif len(self.bigHeap) > len(self.smallHeap) + 1:
            value = heapq.heappop(self.bigHeap)
            heapq.heappush(self.smallHeap, -value)

    def findMedian(self) -> float:
        # If one heap has more elements, its top is the median.
        if len(self.smallHeap) > len(self.bigHeap):
            return float(-self.smallHeap[0])

        if len(self.bigHeap) > len(self.smallHeap):
            return float(self.bigHeap[0])

        # If both heaps have equal size,
        # median is the average of their top elements.
        return (-self.smallHeap[0] + self.bigHeap[0]) / 2