from typing import List 

def moveZeroes(nums: List[int]) -> None:
    """
    Move all zeros to the end of the list in-place with the minimum number of swaps.
    """
    pos = 0  # Position to place the next non-zero element

    for i in range(len(nums)):
        if nums[i] != 0:
            if i != pos:
                nums[pos], nums[i] = nums[i], nums[pos]
            pos += 1