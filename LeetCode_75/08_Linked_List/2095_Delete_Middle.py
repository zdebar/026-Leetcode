from typing import Optional

class ListNode:
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next

def deleteMiddle(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head or not head.next:
        return None  # Edge case: list has 0 or 1 node

    slow = head
    fast = head
    prev = None

    while fast and fast.next:
        prev = slow
        if slow is not None:
            slow = slow.next
        fast = fast.next.next

    # Delete the middle node
    if prev is not None and slow is not None:
        prev.next = slow.next