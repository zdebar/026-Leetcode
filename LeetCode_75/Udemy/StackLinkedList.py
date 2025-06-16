from typing import Optional, Generator

#   Created by Elshad Karimov on 23/05/2020.
#   Copyright © 2020 AppMillers. All rights reserved.

class Node:
    def __init__(self, value: Optional[int] = None):
        self.value: Optional[int] = value
        self.next: Optional[Node] = None

class LinkedList:
    def __init__(self):
        self.head: Optional[Node] = None

    def __iter__(self) -> Generator[Node, None, None]:
        curNode = self.head
        while curNode:
            yield curNode
            curNode = curNode.next

class Stack:
    def __init__(self):
        self.LinkedList: LinkedList = LinkedList()

    def __str__(self) -> str:
        values = [str(x.value) for x in self.LinkedList]
        return '\n'.join(values)

    def isEmpty(self) -> bool:
        return self.LinkedList.head is None

    def push(self, value: int) -> None:
        node = Node(value)
        node.next = self.LinkedList.head
        self.LinkedList.head = node

    def pop(self) -> Optional[int]:
        if self.isEmpty() or self.LinkedList.head is None:
            return None
        else:
            nodeValue = self.LinkedList.head.value
            self.LinkedList.head = self.LinkedList.head.next
            return nodeValue

    def peek(self) -> Optional[int]:
        if self.isEmpty() or self.LinkedList.head is None:
            return None
        else:
            return self.LinkedList.head.value

    def delete(self) -> None:
        self.LinkedList.head = None



customStack = Stack()
customStack.push(1)
customStack.push(2)
customStack.push(3)

print(customStack.peek())

