from typing import List

def kidsWithCandies(candies: List[int], extraCandies: int) -> List[bool]:
    maxCandies = max(candies)
    result: List[bool] = []

    for kid in candies:
        result.append((kid + extraCandies) >= maxCandies)

    return result