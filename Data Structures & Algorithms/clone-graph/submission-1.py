"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        seen = {node}
        stack = [node]
        node_map = {node:Node(node.val)}
        while stack:
            curr = stack.pop()

            for neighbor in curr.neighbors:
                if neighbor not in node_map:
                    node_map[neighbor] = Node(neighbor.val)
                
                node_map[curr].neighbors.append(node_map[neighbor])

                if neighbor not in seen:
                    seen.add(neighbor)
                    stack.append(neighbor)
        
        return node_map[node]


            
        