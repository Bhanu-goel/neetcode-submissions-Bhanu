# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prev_group = dummy
        while True:
            kth = prev_group
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next
            
            strtgrp = prev_group.next
            nxtgrp = kth.next

            prev = nxtgrp
            curr = strtgrp

            while nxtgrp != curr:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            
            prev_group.next = kth
            prev_group = strtgrp

