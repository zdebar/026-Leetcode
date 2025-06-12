from collections import Counter
from typing import List

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count = Counter(nums)
        oper = 0

        for num in list(count):
            complement = k - num
            if complement in count:
                if num == complement:
                    oper += count[num] // 2
                else:
                    pairs = min(count[num], count[complement])
                    oper += pairs
                    count[num] = 0
                    count[complement] = 0

        return oper