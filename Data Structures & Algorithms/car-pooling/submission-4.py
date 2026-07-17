from typing import List
import heapq

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:

        # The car moves only east, so process trips in the order
        # in which passengers are picked up.
        trips.sort(key=lambda t: t[1])

        # Min heap stores all trips that are currently active.
        # Each entry: [drop_off_location, number_of_passengers]
        # The trip ending the earliest stays at the top.
        minHeap = []

        # Current number of passengers inside the car.
        currPass = 0

        for numPass, start, end in trips:

            # Before picking up new passengers at 'start',
            # remove every trip that has already ended.
            # (Passengers whose destination <= current pickup point
            # have already left the car.)
            while minHeap and minHeap[0][0] <= start:
                passengers = heapq.heappop(minHeap)[1]
                currPass -= passengers

            # Pick up passengers for the current trip.
            currPass += numPass

            # If capacity is exceeded at any point,
            # completing all trips is impossible.
            if currPass > capacity:
                return False

            # This trip is now active until 'end',
            # so add it to the heap.
            heapq.heappush(minHeap, [end, numPass])

        # Capacity was never exceeded.
        return True