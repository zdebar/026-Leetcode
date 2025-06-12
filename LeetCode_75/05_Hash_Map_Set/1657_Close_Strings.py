from collections import Counter

def closeStrings(word1: str, word2: str) -> bool:
    # Step 1: Count character frequencies
    count1 = Counter(word1)
    count2 = Counter(word2)

    # Step 2: Check same set of characters
    if set(count1.keys()) != set(count2.keys()):
        return False

    # Step 3: Check if sorted frequency counts are equal
    return sorted(count1.values()) == sorted(count2.values())