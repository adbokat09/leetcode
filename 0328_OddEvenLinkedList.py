from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next: ListNode = next


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


def print_linked_list(head: ListNode) -> None:
    current = head
    end = '->'
    while current:
        if not current.next:
            end = '\n'

        print(current.val, end=end)
        current = current.next


class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not (head and head.next):
            return

        odd_head, odd, even_head, even = None, None, None, None

        i, cur = 1, head

        while cur:
            node = ListNode(cur.val)
            if i % 2 == 1:
                if odd:
                    odd.next = node
                odd = node
                if not odd_head:
                    odd_head = odd
            else:
                if even:
                    even.next = node
                even = node
                if not even_head:
                    even_head = even
            cur = cur.next
            i += 1

        odd.next = even_head
        return odd_head


head = array_to_linked_list([1,2,3,4,5])
print_linked_list(Solution().deleteMiddle(head))
