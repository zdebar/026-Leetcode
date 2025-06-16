#   Created by Elshad Karimov on 22/05/2020.
#   Copyright © 2020 AppMillers. All rights reserved.
from typing import List, Union

class Stack:
    def __init__(self, maxSize: int):
        self.maxSize: int = maxSize
        self.list: List[int] = []

    def __str__(self) -> str:
        self.list.reverse()
        values = [str(x) for x in self.list]
        self.list.reverse()  # Restore original order
        return '\n'.join(values)

    # isEmpty
    def isEmpty(self) -> bool:
        return self.list == []

    # isFull
    def isFull(self) -> bool:
        return len(self.list) == self.maxSize

    # Push
    def push(self, value: int) -> str:
        if self.isFull():
            return "The stack is full"
        else:
            self.list.append(value)
            return "The element has been successfully inserted"

    # Pop
    def pop(self) -> Union[int, str]:
        if self.isEmpty():
            return "There is not any element in the stack"
        else:
            return self.list.pop()

    # Peek
    def peek(self) -> Union[int, str]:
        if self.isEmpty():
            return "There is not any element in the stack"
        else:
            return self.list[len(self.list) - 1]

    # Delete
    def delete(self) -> None:
        self.list = []

customStack = Stack(4)
print(customStack.isEmpty())
print(customStack.isFull())
customStack.push(1)
customStack.push(2)
customStack.push(3)
print(customStack)

