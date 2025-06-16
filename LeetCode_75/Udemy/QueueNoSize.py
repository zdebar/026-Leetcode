#   Created by Elshad Karimov on 29/05/2020.
#   Copyright © 2020 AppMillers. All rights reserved.
from typing import List, Union

class Queue:
    def __init__(self):
        self.items: List[int] = []
    
    def __str__(self) -> str:
        values = [str(x) for x in self.items]
        return ' '.join(values)
    
    def isEmpty(self) -> bool:
        return self.items == []
    
    def enqueue(self, value: int) -> str:
        self.items.append(value)
        return "The element is inserted at the end of Queue"
    
    def dequeue(self) -> Union[int, str]:
        if self.isEmpty():
            return "There is not any element in the Queue"
        else:
            return self.items.pop(0)
    
    def peek(self) -> Union[int, str]:
        if self.isEmpty():
            return "There is not any element in the Queue"
        else:
            return self.items[0]
    
    def delete(self) -> None:
        self.items = []




customQueue = Queue()
customQueue.enqueue(1)
customQueue.enqueue(2)
customQueue.enqueue(3)
print(customQueue.peek())
customQueue.delete()
