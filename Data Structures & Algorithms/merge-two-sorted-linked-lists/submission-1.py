# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        lst = []
        while list1 or list2:
            if list1:
                lst.append(list1.val)
                list1 = list1.next
            if list2:
                lst.append(list2.val)
                list2 = list2.next
        if len(lst) == 0:
            return
        if len(lst) == 1:
            return ListNode(lst[0])
        lst.sort()
        head = ListNode(lst[0])
        hd = head
        for i in range(1,len(lst)):
            node = ListNode(lst[i])
            head.next = node
            head = node
        return hd
