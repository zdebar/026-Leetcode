from typing import List, Union

#   Created by Elshad Karimov on 29/05/2020.
#   Copyright © 2020 AppMillers. All rights reserved.

class Queue:
    def __init__(self, maxSize: int):
        self.items: List[Union[int, None]] = [None for _ in range(maxSize)]
        self.maxSize: int = maxSize
        self.start: int = -1
        self.top: int = -1 
    
    def __str__(self) -> str:
        values = [str(x) if x is not None else "None" for x in self.items]
        return ' '.join(values)
    
    def isFull(self) -> bool:
        if self.top + 1 == self.start:
            return True
        elif self.start == 0 and self.top + 1 == self.maxSize:
            return True
        else:
            return False
    
    def isEmpty(self) -> bool:
        return self.top == -1
    
    def enqueue(self, value: int) -> str:
        if self.isFull():
            return "The queue is full"
        else:
            if self.top + 1 == self.maxSize:
                self.top = 0
            else:
                self.top += 1
                if self.start == -1:
                    self.start = 0
            self.items[self.top] = value
            return "The element is inserted at the end of Queue"
    
    def dequeue(self) -> Union[int, str]:
        if self.isEmpty():
            return "There is not any element in the Queue"
        else:
            firstElement = self.items[self.start]
            start = self.start
            if self.start == self.top:
                self.start = -1
                self.top = -1
            elif self.start + 1 == self.maxSize:
                self.start = 0
            else:
                self.start += 1
            self.items[start] = None
            return firstElement if firstElement is not None else "Invalid state"
    
    def peek(self) -> Union[int, str]:
        if self.isEmpty():
            return "There is not any element in the Queue"
        else:
            element = self.items[self.start]
            return element if element is not None else "Invalid state"
    
    def delete(self) -> None:
        self.items = [None for _ in range(self.maxSize)]
        self.top = -1
        self.start = -1






customQueue = Queue(3)
customQueue.enqueue(1)
customQueue.enqueue(2)
customQueue.enqueue(3)
customQueue.delete()
print(customQueue)