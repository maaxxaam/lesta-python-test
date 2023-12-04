from typing import List
from random import randint
from time import perf_counter

def quickSort(array, low = 0, high = None):
    if high is None:
        high = len(array) - 1
    while low < high:
        # choose pivot as median between first, last and mid values
        pivot_candidates = [high, low, low + ((high - low) // 2)]
        pivot_vals = [array[i] for i in pivot_candidates]
        pivot = sum(pivot_vals) - min(pivot_vals) - max(pivot_vals)
        pivot_index = pivot_candidates[pivot_vals.index(pivot)]
        # pointer to pivot endpoint
        i = low
    
        for j in range(low, high + 1):
            if j == pivot_index:
                continue
            if array[j] <= pivot:
                (array[i], array[j]) = (array[j], array[i])
                if i == pivot_index:
                    pivot_index = j
                i += 1
    
        # move pivot to match partition
        (array[i], array[pivot_index]) = (array[pivot_index], array[i])
        pivot = i
        # make recursive call to smaller region
        if pivot - low < high - pivot:
            quickSort(array, low, pivot - 1)
            low = pivot + 1
        else:
            quickSort(array, pivot + 1, high)
            high = pivot - 1

if __name__ == "__main__":
    toSort = [list() for _ in range(10)]
    for i in range(10):
        toSort[i] = [randint(0, 10**9) for _ in range(16)]
    start = perf_counter()
    for i in range(10):
        quickSort(toSort[i])
    end = perf_counter()
    print((end - start) / 10)
