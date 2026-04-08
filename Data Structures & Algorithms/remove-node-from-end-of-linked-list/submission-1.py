# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def length(head):
    hd = head
    l = 0
    while hd:
        l+=1
        hd = hd.next
    return l
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l = length(head)
        if n == 1 and l == 1:
            return 
        removeidx = l - n
        if removeidx == 0:
            return head.next
        hd = head
        prev = None
        while removeidx > 0:
            prev = hd
            hd = hd.next
            removeidx-=1
        prev.next = hd.next
        return head