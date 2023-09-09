from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next: ListNode = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous, current = None, head
        while current:
            next_ = current.next
            current.next = previous
            previous = current
            current = next_
        return previous


    def pairSum(self, head: Optional[ListNode]) -> int:
        slow, fast = head, head
        while fast and fast.next:
            slow = fast
            fast = fast.next.next

        head2 = self.reverseList(slow)

        max_sum = float('-inf')
        while head2:
            max_sum = max(max_sum, head.val + head2.val)
            head, head2 = head.next, head2.next

        return max_sum
