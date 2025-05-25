def reverseVowels(s: str) -> str:
    vowels = set("aeiouAEIOU")
    chars: list[str] = list(s)
    i, j = 0, len(chars) - 1

    while i < j:
        while i < j and chars[i] not in vowels:
            i += 1
        while i < j and chars[j] not in vowels:
            j -= 1
        chars[i], chars[j] = chars[j], chars[i]

        j -= 1
        i += 1
    
    return "".join(chars)