# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        z=[]
        head1=head
        while head1:
            z.append(head1.val)
            head1=head1.next
        n=(len(z)//k)*k
        f=z[n:]
        p=[]
        for i in range(0,n,k):
            p+=z[i:i+k][::-1]
        p+=f
        dummy=present=ListNode(0)
        for i in p:
            dummy.next=ListNode(i)
            dummy=dummy.next
        return present.next
