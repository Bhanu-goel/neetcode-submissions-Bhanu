# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = 0
        while l1:
            num1 = num1*10+l1.val
            l1 = l1.next
        num2 = 0
        while l2:
            num2 = num2*10+l2.val
            l2 = l2.next
        s1 = int(str(num1)[::-1])
        s2 = int(str(num2)[::-1])
        print(s1,s2)
        s = str(s1+s2)[::-1]
        dummy = ListNode(-1)
        curr = dummy
        for i in s:
            print(i)
            node = ListNode(int(i))
            curr.next = node
            curr = curr.next
        return dummy.next