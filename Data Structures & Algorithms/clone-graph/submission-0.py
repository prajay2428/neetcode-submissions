"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        stack = [node]
        seen = set()
        node_map = {}
        if not node:
            return None

        while stack:
            curr = stack.pop()
            seen.add(curr)
            new_node = Node(curr.val)
            node_map[curr] = new_node
            if curr.neighbors is not None:
                for nodes in curr.neighbors:
                    if nodes not in seen:
                        stack.append(nodes)

        stack = [node]
        seen = set()
        while stack:
            curr = stack.pop()
            seen.add(curr)
            if curr.neighbors is not None:
                node_map[curr].neighbors = []
                for nodes in curr.neighbors:
                    node_map[curr].neighbors.append(node_map[nodes])
            if curr.neighbors is not None:
                for nodes in curr.neighbors:
                    if nodes not in seen:
                        stack.append(nodes)
        return node_map[node]
        
        
            
        