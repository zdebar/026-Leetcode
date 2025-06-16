from typing import Optional, Generator

#   Created by Elshad Karimov on 30/05/2020.
#   Copyright © 2020 AppMillers. All rights reserved.


class Node:
    def __init__(self, value: Optional[int] = None):
        self.value: Optional[int] = value
        self.next: Optional[Node] = None

    def __str__(self) -> str:
        return str(self.value)

class LinkedList:
    def __init__(self):
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None

    def __iter__(self) -> Generator[Node, None, None]:
        curNode = self.head
        while curNode:
            yield curNode
            curNode = curNode.next

class Queue:
    def __init__(self):
        self.linkedList: LinkedList = LinkedList()

    def __str__(self) -> str:
        values = [str(x) for x in self.linkedList]
        return ' '.join(values)

    def enqueue(self, value: int) -> None:
        newNode = Node(value)
        if self.linkedList.head is None:
            self.linkedList.head = newNode
            self.linkedList.tail = newNode
        else:
            assert self.linkedList.tail is not None
            self.linkedList.tail.next = newNode
            self.linkedList.tail = newNode

    def isEmpty(self) -> bool:
        return self.linkedList.head is None

    def dequeue(self) -> Optional[Node]:
        if self.isEmpty():
            return None
        else:
            tempNode = self.linkedList.head
            if self.linkedList.head == self.linkedList.tail:
                self.linkedList.head = None
                self.linkedList.tail = None
            else:
                assert self.linkedList.head is not None
                self.linkedList.head = self.linkedList.head.next
            return tempNode

    def peek(self) -> Optional[Node]:
        if self.isEmpty():
            return None
        else:
            return self.linkedList.head

    def delete(self) -> None:
        self.linkedList.head = None
        self.linkedList.tail = None




custQueue = Queue()
custQueue.enqueue(1)
custQueue.enqueue(2)
custQueue.enqueue(3)
print(custQueue)
print(custQueue.peek())
print(custQueue)