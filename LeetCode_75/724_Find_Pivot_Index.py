from typing import List

def pivotIndex( nums: List[int]) -> int:   
    left = 0
    right = sum(nums[1:])

    if len(nums) == 1 or left == right: return 0

    for i in range(1,len(nums)):
        right -= nums[i]
        left += nums[i - 1]
        if right == left: return i        

    return -1