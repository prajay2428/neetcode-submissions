# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        curr1 = p
        curr2 = q
        stack1=[]
        stack2 = []
        res1=[]
        res2 = []
        while curr1 or stack1:
            while curr1:
                stack1.append(curr1)
                curr1 = curr1.left
                if curr1 == None:
                    stack1.append("null")

            while stack1[-1] == "null":
                stack1.pop()
                res1.append("null")

            curr1 = stack1.pop()
            res1.append(curr1.val)
            curr1 = curr1.right
        while curr2 or stack2:
            while curr2:
                stack2.append(curr2)
                curr2 = curr2.left
                if curr2 == None:
                    stack2.append("null")
            while stack2[-1] == "null":
                stack2.pop()
                res2.append("null")
            
            curr2 = stack2.pop()
            res2.append(curr2.val)
            curr2 = curr2.right

        return res1 == res2

        

        