def isSubsequence( s: str, t: str) -> bool:

    if not s: return True

    end = len(s)
    i = 0

    for char in t:
        if char == s[i]:
            i += 1
            if i == end: 
                return True

    return False