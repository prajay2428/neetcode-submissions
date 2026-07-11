# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.index = -1
        self.inorder = []
        stack =[]
        curr = root
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            self.inorder.append(curr.val)
            curr = curr.right
        

        

    def next(self) -> int:
        self.index += 1
        return self.inorder[self.index]
        
        

    def hasNext(self) -> bool:
        return self.index != len(self.inorder)-1
        
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()