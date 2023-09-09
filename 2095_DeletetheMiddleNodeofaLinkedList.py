from typing import Optional
from time import time


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next: ListNode = next


def print_linked_list(head: ListNode) -> None:
    current = head
    end = '->'
    while current:
        if not current.next:
            end = '\n'

        print(current.val, end=end)
        current = current.next


def array_to_linked_list(lst: list) -> ListNode:
    head = None
    current = None
    for el in lst:
        node = ListNode(el)

        if not head:
            head = node

        if current:
            current.next = node

        current = node

    return head


# class Solution:
#     def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         if not (head and head.next):
#             return
#
#         count_el = 0
#         el = head
#         while el:
#             count_el += 1
#             el = el.next
#
#         center = count_el // 2
#
#         last_el, el = head, head
#         for i in range(center ):
#             last_el = el
#             el = el.next
#
#         last_el.next = el.next
#         return head


class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not (head and head.next):
            return

        last_el, slow_el, fast_el = head, head, head
        while fast_el and fast_el.next:
            last_el = slow_el
            slow_el = slow_el.next
            fast_el = fast_el.next.next

        last_el.next = slow_el.next
        return head


head = array_to_linked_list(range(100_000))
start = time()
print_linked_list(Solution().deleteMiddle(head))
end = time()
print(end - start)
