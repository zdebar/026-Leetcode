from typing import List

def findMaxAverage(nums: List[int], k: int) -> float:
    windowSum = sum(nums[:k])
    maxSum = windowSum

    for i in range(k, len(nums)):
        windowSum += nums[i] - nums[i - k]
        maxSum = max(maxSum, windowSum)

    return maxSum / k