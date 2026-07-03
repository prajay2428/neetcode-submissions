# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        def insert(node,val):
            if val < node.val and node.left is None:
                node.left = TreeNode(val)
                
            
            elif val > node.val and node.right is None:
                node.right = TreeNode(val)
                
            
            elif val < node.val and node.left is not None:
                return insert(node.left,val)

            elif val > node.val and node.right is not None:
                return insert(node.right,val)
        
        insert(root,val)

        return root
        