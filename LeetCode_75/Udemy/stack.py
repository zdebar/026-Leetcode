#   Created by Elshad Karimov on 19/05/2020.
#   Copyright © 2020 AppMillers. All rights reserved.
from typing import List

class MultiStack:
    def __init__(self, stacksize: int):
        self.numstacks: int = 3
        self.array: List[int] = [0] * (stacksize * self.numstacks)
        self.sizes: List[int] = [0] * self.numstacks
        self.stacksize: int = stacksize

    def Push(self, item: int, stacknum: int) -> None:
        if self.IsFull(stacknum):
            raise Exception('Stack is full')
        self.sizes[stacknum] += 1
        self.array[self.IndexOfTop(stacknum)] = item

    def Pop(self, stacknum: int) -> int:
        if self.IsEmpty(stacknum):
            raise Exception('Stack is empty')
        value: int = self.array[self.IndexOfTop(stacknum)]
        self.array[self.IndexOfTop(stacknum)] = 0
        self.sizes[stacknum] -= 1
        return value

    def Peek(self, stacknum: int) -> int:
        if self.IsEmpty(stacknum):
            raise Exception('Stack is empty')
        return self.array[self.IndexOfTop(stacknum)]

    def IsEmpty(self, stacknum: int) -> bool:
        return self.sizes[stacknum] == 0

    def IsFull(self, stacknum: int) -> bool:
        return self.sizes[stacknum] == self.stacksize

    def IndexOfTop(self, stacknum: int) -> int:
        offset: int = stacknum * self.stacksize
        return offset + self.sizes[stacknum] - 1

stack = MultiStack(1)

