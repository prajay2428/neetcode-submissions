# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans = []
        number =str(root.val)
        stack = [(root,number)]
        while stack:
            node, number = stack.pop()
            if not node.right and not node.left:
                ans.append(number)
            if node.right:
                stack.append((node.right,number+str(node.right.val)))
            
            if node.left:
                stack.append((node.left,number+str(node.left.val)))
        sum =0
        for s in ans:
            sum += int(s)

        return sum

        

