from typing import List

def increasingTriplet(nums: List[int]) -> bool:
    max1, max2 = float('inf'), float('inf')
    for i in nums:
        if i > max2: return True
        if i >= max1: max2 = i
        else: max1 = i
    return False