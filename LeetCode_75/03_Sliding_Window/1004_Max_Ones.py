from typing import List

def longestOnes(nums: List[int], k: int) -> int:
    left = 0
    max_length = 0
    zeros_flipped = 0

    for right in range(len(nums)):
        if nums[right] == 0:
            zeros_flipped += 1
        
        while zeros_flipped > k:
            if nums[left] == 0:
                zeros_flipped -= 1
            left += 1
        
        max_length = max(max_length, right - left + 1)

    return max_length