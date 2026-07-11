# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        ans = []
        queue = deque()
        queue.append(root)
        direction = 1
        while queue:
            n = len(queue)
            level = [] 
            for _ in range(n):
                node = queue.popleft()
                level.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            if direction == 1:
                ans.append(level)
            else:
                ans.append(level[::-1])
            direction *= -1
        return ans