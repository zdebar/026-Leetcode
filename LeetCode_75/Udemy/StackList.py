#   Created by Elshad Karimov on 22/05/2020.
#   Copyright © 2020 AppMillers. All rights reserved.

from typing import List, Union

class Stack:
    def __init__(self):
        self.list: List[int] = []
    
    def __str__(self) -> str:
        self.list.reverse()
        values = [str(x) for x in self.list]
        self.list.reverse()  # Restore original order
        return '\n'.join(values)
    
    # isEmpty
    def isEmpty(self) -> bool:
        return self.list == []
    # push
    def push(self, value: int) -> str:
        self.list.append(value)
        return "The element has been successfully inserted"

    # pop
    def pop(self) -> Union[int, str]:
        if self.isEmpty():
            return "There is not any element in the stack"
        else:
            return self.list.pop()
    
    # peek
    def peek(self) -> Union[int, str]:
        if self.isEmpty():
            return "There is not any element in the stack"
        else:
            return self.list[len(self.list) - 1]
    
    # delete
    def delete(self) -> None:
        self.list = []




customStack = Stack()
customStack.push(1)
customStack.push(2)
customStack.push(3)
print(customStack.peek())
print(customStack)
