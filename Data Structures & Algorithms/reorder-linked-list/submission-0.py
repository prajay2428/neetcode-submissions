# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        fast = head
        slow = head

        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        

        curr = slow.next
        slow.next = None
        prev = None

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            
        

        
        # prev is the head of the second cycle
        # now the second cycle is reversed
        # we need to join those two 

        head2 = prev
        head1 = head
        while head2:
            temp1 = head1.next
            temp2 = head2.next

            head1.next = head2
            head2.next = temp1

            head1 = temp1
            head2 = temp2

        