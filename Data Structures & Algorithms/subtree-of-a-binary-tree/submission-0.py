# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSame(p, q):
            if p is None and q is None:
                return True

            if p is None and q is not None:
                return False

            if q is None and p is not None:
                return False

            if p.val != q.val:
                return False

            return isSame(p.left, q.left) and isSame(p.right, q.right)

        stack = []
        curr = root
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()
            
            if curr.val == subRoot.val:
                print(curr.val,subRoot.val)
                res = isSame(curr,subRoot)
                if res == True:
                    return True
                
            curr = curr.right
        
        return False

       
