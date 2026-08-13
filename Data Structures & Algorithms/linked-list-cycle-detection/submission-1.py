# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr = head

        while curr:
            if curr.val == 'v':
                return True

            curr.val = 'v'
            curr = curr.next
        

        return False
        