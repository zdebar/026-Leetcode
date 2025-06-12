from typing import List

def maxArea(height: List[int]) -> int:
    i, j = 0, len(height) - 1
    max_area = 0

    while i < j:
        left, right = height[i], height[j]
        area = min(left, right) * (j - i)
        max_area = max(max_area, area)

        if left < right:
            while i < j and height[i] <= left:
                i += 1
        else:
            while i < j and height[j] <= right:
                j -= 1

    return max_area
