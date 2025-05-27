from typing import List

def kidsWithCandies(candies: List[int], extraCandies: int) -> List[bool]:
    maxCandy = max(candies) 
    
    output: List[bool] = []
    for candy in candies:
        if candy + extraCandies >= maxCandy:
            output.append(True) 
        else:
            output.append(False)
            
    return output