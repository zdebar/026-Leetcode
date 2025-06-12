from collections import Counter
from typing import List

def uniqueOccurrences(arr: List[int]) -> bool:
    count = Counter(arr) 
    occurrences = count.values() 
    return len(set(occurrences)) == len(occurrences)