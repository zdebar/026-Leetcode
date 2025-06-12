from typing import List

def productExceptSelf(nums: List[int]) -> List[int]:
    n = len(nums)
    output = [1] * n

    helper = 1
    for i in range(n):
        output[i] = helper
        helper *= nums[i]

    helper = 1
    for i in range(n - 1, -1, -1):
        output[i] *= helper
        helper *= nums[i]

    return output