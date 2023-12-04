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
            if pivot - low < 16:
                insertionSort(array, low, pivot - 1)
            else:
                quickSort(array, low, pivot - 1)
            low = pivot + 1
        else:
            if high - pivot < 16:
                insertionSort(array, pivot + 1, high)
            else:
                quickSort(array, pivot + 1, high)
            high = pivot - 1

def insertionSort(array, low = 0, high = None):
    if high is None:
        high = len(array)
    for step in range(low + 1, high):
        key = array[step]
        j = step - 1

        while j >= low and key < array[j]:
            array[j + 1] = array[j]
            j -= 1

        array[j + 1] = key


if __name__ == "__main__":
    sizes = [20*i for i in range(5, 20)]
    samples = 40
    for size in sizes:
        print("Testing size", size)
        toSort = [list() for _ in range(samples)]
        for i in range(samples):
            toSort[i] = [randint(0, 10**9) for _ in range(size)]
        start = perf_counter()
        for i in range(samples):
            quickSort(toSort[i])
        end = perf_counter()
        print(f"Quick: {(end - start):.6f}", end=" ")
        start = perf_counter()
        for i in range(samples):
            insertionSort(toSort[i])
        end = perf_counter()
        print(f"Insert: {(end - start):.6f}")
