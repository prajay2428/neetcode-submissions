"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        queue = deque()
        queue.append(root)
        ans =[]
        while queue:
            n = len(queue)
            ans = []
            for _ in range(n):
                node = queue.popleft()
                ans.append(node)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            
            for i in range(len(ans)):
                if i == len(ans)-1:
                    ans[i].next = None
                    continue
                else:
                    ans[i].next = ans[i+1]
        return root 
                    
        