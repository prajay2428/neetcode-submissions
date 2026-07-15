import heapq
from typing import List


class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # pending heap:
        # (enqueue_time, processing_time, original_index)
        pending = []

        for index, (enqueue_time, processing_time) in enumerate(tasks):
            pending.append((enqueue_time, processing_time, index))

        heapq.heapify(pending)

        # available heap:
        # (processing_time, original_index)
        available = []

        order = []
        time = 0

        while pending or available:

            # If the CPU is idle, jump to the next task's enqueue time.
            if not available and pending and time < pending[0][0]:
                time = pending[0][0]

            # Add every task that is available at the current time.
            while pending and pending[0][0] <= time:
                enqueue_time, processing_time, index = heapq.heappop(pending)

                heapq.heappush(
                    available,
                    (processing_time, index)
                )

            # Execute the shortest available task.
            processing_time, index = heapq.heappop(available)

            time += processing_time
            order.append(index)

        return order