"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hashmap = {}
        curr = head
        while curr:
            hashmap[curr] = Node(curr.val)
            curr = curr.next
        
        for node in hashmap:
            hashmap[node].next = hashmap.get(node.next)
            hashmap[node].random = hashmap.get(node.random)

        
        return hashmap.get(head)

        

        

        