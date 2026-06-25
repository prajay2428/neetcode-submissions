# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
        
        new_n = length - n

        if length == n:
            return head.next
        
        node = head
        while new_n > 0:
            node = node.next
            new_n -= 1
        
        # we got the node
        prev = head
        curr = head
        while curr:
            if curr == node:
                temp = curr.next
                prev.next = temp
                curr.next = None
            prev = curr
            curr = curr.next
        return head



            


            
        