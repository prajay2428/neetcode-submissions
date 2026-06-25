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
        
        n_to_be_changed = length - n - 1

        if length == n:
            return head.next
        curr = head
        
        while n_to_be_changed > 0:
            curr = curr.next
            n_to_be_changed -= 1
        
        curr.next = curr.next.next
        return head
            


        
        
        
        
        



            


            
        