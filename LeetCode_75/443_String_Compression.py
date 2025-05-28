from typing import List

def compress(chars: List[str]) -> int:
    i = 0  # read pointer
    j = 0  # write pointer
    
    while i < len(chars):
        char = chars[i]
        count = 0
        while i < len(chars) and chars[i] == char:
            i += 1
            count += 1
        chars[j] = char
        j += 1
        if count > 1:
            for c in str(count):
                chars[j] = c
                j += 1
    return j