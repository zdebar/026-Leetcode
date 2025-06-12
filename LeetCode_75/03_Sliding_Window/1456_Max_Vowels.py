def maxVowels(s: str, k: int) -> int:
    vowels = set('aeiou')
    best = sum(1 for i in range(k) if s[i] in vowels)

    curr = best
    for i in range(k, len(s)):
        if k == best: 
            return k
        if s[i] in vowels:
            curr += 1
        if s[i - k] in vowels:
            curr -= 1
        best = max(best, curr)

    return best