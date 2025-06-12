def gcdOfStrings( str1: str, str2: str) -> str:
    from math import gcd

    if str1 + str2 != str2 + str1:
        return ""

    gcd_length = gcd(len(str1),len(str2))

    return str1[:gcd_length]

def gcd(a: int, b: int) -> int:
    while b != 0:
        a, b = b, a % b
    return a