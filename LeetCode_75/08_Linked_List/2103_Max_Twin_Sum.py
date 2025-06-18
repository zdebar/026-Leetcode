from typing import Optional

class ListNode:
    def __init__(self, val: int = 0, next: 'Optional[ListNode]' = None):
        self.val = val
        self.next = next

def pairSum(head: Optional[ListNode]) -> int:
    slow = head
    fast = head

    while fast and fast.next:
        if slow is not None:
            slow = slow.next
        fast = fast.next.next

    prev = None
    curr = slow
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node

    max_sum = 0
    first = head
    second = prev  # reversed second half

    while first is not None and second is not None:
        max_sum = max(max_sum, first.val + second.val)
        first = first.next
        second = second.next

    return max_sum