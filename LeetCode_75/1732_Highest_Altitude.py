from typing import List

def largestAltitude(gain: List[int]) -> int:
    maxAlt = 0
    curAlt = 0

    for trip in gain:
        curAlt += trip
        maxAlt = max(maxAlt, curAlt)
        
    return maxAlt