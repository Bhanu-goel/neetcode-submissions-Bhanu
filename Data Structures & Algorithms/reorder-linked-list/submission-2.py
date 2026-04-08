# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def reverse(head):
    prev = None
    curr = head
    while curr:
        nextnode = curr.next
        curr.next = prev
        prev = curr
        curr = nextnode
    return prev
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head.next == None or head.next.next == None:
            return
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        head2 = reverse(slow.next)
        slow.next = None
        head1 = head

        while head2:
            temp1 = head1.next
            temp2 = head2.next

            head1.next = head2
            head2.next = temp1

            head1 = temp1
            head2 = temp2


