def isSubsequence( s: str, t: str) -> bool:

    if not s: return True

    i = 0
    for char in t:
        if char == s[i]:
            i += 1
            if i == len(s): return True

    return False