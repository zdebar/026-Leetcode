from collections import Counter
from typing import List

def equalPairs(grid: List[List[int]]) -> int:
    row_counts = Counter(tuple(row) for row in grid)
 
    count = 0
    for col in zip(*grid):
        count += row_counts[tuple(col)]

    return count