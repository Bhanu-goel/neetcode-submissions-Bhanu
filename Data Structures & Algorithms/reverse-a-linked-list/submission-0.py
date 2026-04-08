# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        lst = []
        hd = head
        while hd:
            lst.append(hd.val)
            hd = hd.next
        lst = lst[::-1]
        i=0
        hd = head
        while head:
            head.val = lst[i]
            i+=1
            head = head.next
        return hd