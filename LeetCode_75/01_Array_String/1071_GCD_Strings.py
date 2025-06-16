def gcdOfStrings( str1: str, str2: str) -> str:
    def gdc (a:int, b:int) -> int:
        while b != 0:
            a, b = b, a % b
        return a

    if str1 + str2 != str2 + str1:
        return ""

    s = gdc(len(str1), len(str2))
    return str1[:s]