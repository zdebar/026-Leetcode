from typing import List

def removeStars(s: str) -> str:
    stack: List[str] = []

    for char in s:
        if char == "*":
            if stack:
                stack.pop()
        else:
            stack.append(char)
    
    return "".join(stack)