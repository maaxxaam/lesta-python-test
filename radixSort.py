from typing import List
from random import randint
from time import perf_counter

def radixSort(array: List[int]):
    max_element = max(array)
    size = len(array)
    output = array.copy()
    place = 0
    shift = 0
    
    while max_element >> shift > 0:
        count = [0] * 256
        # Calculate buckets
        for item in array:
            index = (item >> shift) & 255
            count[index] += 1
    
        # Calculate cumulative count
        for i in range(1, 256):
            count[i] += count[i - 1]

        # Place elements according to buckets
        for item in array[::-1]:
            index = (item >> shift) & 255
            count[index] -= 1
            output[count[index]] = item

        # Shift to the next byte
        array = output.copy()
        place += 1
        shift = place << 3

if __name__ == "__main__":
    toSort = [list() for _ in range(10)]
    for i in range(10):
        toSort[i] = [randint(0, 10**9) for _ in range(10**7)]
    start = perf_counter()
    for i in range(10):
        radixSort(toSort[i])
    end = perf_counter()
    print((end - start) / 10)

