# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # append the right most element in that level
        

        if not root:
            return []
        
        queue = deque()
        queue.append(root)
        ans = []

        while queue:
            level = []
            n = len(queue)
            for _ in range(n):
                node = queue.popleft()
                level.append(node.val)

                if node.left:queue.append(node.left)
                if node.right:queue.append(node.right)
            ans.append(level[-1])

        return ans
        
        