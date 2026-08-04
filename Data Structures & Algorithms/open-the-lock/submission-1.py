class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        visited = {"0000"}
        queue = deque()
        queue.append(("0000",0))
        if "0000" in deadends:
            return -1
        
        ans = []

        while queue:
            number,distance = queue.popleft()    
            if number == target:
                return distance
            distance += 1
            for i, s in enumerate(number):
                digit = int(s)

                forward = (digit + 1) % 10
                backward = (digit - 1) % 10

                forward_number = (
                    number[:i]
                    + str(forward)
                    + number[i + 1:]
                )

                backward_number = (
                    number[:i]
                    + str(backward)
                    + number[i + 1:]
                )

                if forward_number not in visited and forward_number not in deadends:
                    queue.append((forward_number, distance))
                    visited.add(forward_number)
                
                if backward_number not in visited and backward_number not in deadends:
                    queue.append((backward_number, distance))
                    visited.add(backward_number)
        return -1




        
            

        