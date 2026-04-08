# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        lst = []
        hd = head
        while hd:
            lst.append(hd.val)
            hd = hd.next
        l1,l2 = lst[:len(lst)//2] , lst[len(lst)//2:]
        l1.reverse()
        # print(l1,l2)
        curr = head
        i=1
        while curr:
            if i&1 and l1:
                curr.val = l1.pop()
            else:
                curr.val = l2.pop() 
            curr = curr.next
            i+=1