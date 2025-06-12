from typing import List

def reverseVowels( s: str) -> str:
    vowels = set("aeiouAEIOU")
    i, j = 0, len(s) - 1
    char: List[str] = list(s)

    while i < j:
        while i < j and char[i] not in vowels:
            i += 1
        
        while i < j and char[j] not in vowels:
            j -= 1

        if i < j:
            char[i], char[j] = char[j], char[i]
            i += 1
            j -= 1
    
    return "".join(s)