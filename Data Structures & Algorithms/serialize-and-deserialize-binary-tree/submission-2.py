# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        ans = []
        def dfs(root):
            if root is None:
                ans.append('N')
                return None
            ans.append(str(root.val))
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        
        data = ",".join(ans)
        return data
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        preorder = data.split(",")
        i = [0]
        def dfs():
            if preorder[i[0]] =='N':
                i[0] += 1
                return None
            root = TreeNode(int(preorder[i[0]]))
            i[0] += 1
            root.left = dfs()
            root.right = dfs()
        return root
    


        
