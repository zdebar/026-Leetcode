from typing import List

def increasingTriplet(nums: List[int]) -> bool:
    first = float('inf')
    second = float('inf')
    
    for num in nums:
        if num <= first:
            first = num
        elif num <= second:
            second = num
        else:
            # Found a num greater than both first and second
            return True
    
    return False