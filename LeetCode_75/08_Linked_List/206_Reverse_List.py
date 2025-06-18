from typing import Optional

class ListNode:
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next

def reverseList_iter(head: Optional[ListNode]) -> Optional[ListNode]:
    prev = None
    curr = head
    
    while curr:
        next_node = curr.next  
        curr.next = prev       
        prev = curr           
        curr = next_node      

    return prev

def reverseList( head: Optional[ListNode]) -> Optional[ListNode]:
        # Base case: empty list or single node
        if head is None or head.next is None:
            return head

        # Recursively reverse the rest of the list
        new_head = reverseList(head.next)

        # Reverse the current link
        head.next.next = head
        head.next = None

        return new_head