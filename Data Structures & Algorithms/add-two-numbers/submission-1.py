# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = ListNode(-1)
        curr = dummy
        while l1 and l2:
            num = l1.val + l2.val + carry
            node = ListNode(num%10)
            curr.next = node
            curr = curr.next
            carry = num//10
            l1 = l1.next
            l2 = l2.next
        while l1:
            node = ListNode((l1.val+carry)%10)
            carry = (l1.val+carry)//10
            curr.next = node
            curr = curr.next
            l1 = l1.next

        while l2:
            node = ListNode((l2.val+carry)%10)
            carry = (l2.val+carry)//10
            curr.next = node
            curr = curr.next
            l2 = l2.next
        if carry == 1:
            curr.next = ListNode(carry)
        return dummy.next