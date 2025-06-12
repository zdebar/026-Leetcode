from typing import List

def canPlaceFlowers(flowerbed: List[int], n: int) -> bool:
    count = 0
    length = len(flowerbed)

    for i in range(length):
        if (flowerbed[i] == 0 and (i == 0 or flowerbed[i - 1] == 0) and ((i == length - 1) or flowerbed[i + 1] == 0)):
            flowerbed[i] = 1
            count += 1

    return count >= n