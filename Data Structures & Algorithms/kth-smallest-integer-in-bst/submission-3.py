# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # inorder traversal of a binary search tree will give
        # ascending order of values of nodes
        # so do inorder traversal and increase counter every time you pop
        # when count becomes k we have reached kth smallest element
        stack = []
        ans = []
        count = 0
        curr = root
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            count += 1
            if count ==k:
                return curr.val
            
            curr = curr.right
        
        
        