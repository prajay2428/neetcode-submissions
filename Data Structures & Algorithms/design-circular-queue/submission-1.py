class MyCircularQueue:

    def __init__(self, k: int):
        self.stack = []
        self.front = 0
        self.rear = -1
        self.k = k
        

    def enQueue(self, value: int) -> bool:
        if len(self.stack) == self.k:
            return False
        else:
            self.stack.append(value)
            return True


        
        

    def deQueue(self) -> bool:
        if len(self.stack) == 0:
            return False
        else:
           popped = self.stack.pop(0)
           return True
        

    def Front(self) -> int:
        if not self.stack:
            return -1
        else:
            return self.stack[0]

        

    def Rear(self) -> int:
        if not self.stack:
            return -1
        else:
            return self.stack[-1]
        

    def isEmpty(self) -> bool:
        return len(self.stack) == 0
        

    def isFull(self) -> bool:
        return len(self.stack) == self.k
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()