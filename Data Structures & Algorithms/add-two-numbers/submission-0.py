class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s1=""
        s2=""
        curr1 = l1
        curr2 = l2
        while curr1:
            s1+=str(curr1.val)
            curr1 = curr1.next
        while curr2:
            s2+=str(curr2.val)
            curr2= curr2.next

        print(s1,s2)
        n1 = int(s1[::-1])
        n2 = int(s2[::-1])
        n3 = n1 + n2
        s3 = str(n3)
        l=[]
        for i in range(len(s3)):
            l.append(ListNode(int(s3[i])))
        print(l)

        for i in range(len(l)-1,-1,-1):
            if i==0:
                l[i].next = None
                continue
            l[i].next = l[i-1]

        return l[len(l)-1]