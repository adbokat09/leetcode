from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


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
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous, current = None, head
        while current:
            next_ = current.next
            current.next = previous
            previous = current
            current = next_
        return previous


lst = array_to_linked_list([1, 2, 3, 4, 5])
print_linked_list(lst)
lst = Solution().reverseList(lst)
print_linked_list(lst)
