class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        decimal_value = 0

        current = head
        while current:
            decimal_value = decimal_value * 2 + current.val
            current = current.next

        return decimal_value



''' 

1 0 1 



1, 2, 5  



decimal = 7
currrent =  


'''



