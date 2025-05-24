def mergeAlternately(word1: str, word2: str) -> str:
    result = ""
    length = min(len(word1),len(word2))
    for i in range(length):
        result += word1[i] + word2[i]
    result += word1[length:] + word2[length:]
    return result