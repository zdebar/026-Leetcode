from typing import List

def longestSubarray(nums: List[int]) -> int:
        left = 0
        zeroes = 0
        best = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zeroes += 1

            while zeroes > 1:
                if nums[left] == 0:
                    zeroes -= 1
                left += 1

            best = max(best, right - left)        

        return best