from typing import List
from random import randint
from time import perf_counter
from quickSort import quickSort
from radixSort import radixSort

def mainSort(array: List[int]):
    if len(array) < 80:
        quickSort(array)
    else:
        radixSort(array)

if __name__ == '__main__':
    sizes = [10*i for i in range(3,14)]
    array_count = 40
    algos = {
            'Quick': quickSort,
            'Radix': radixSort
            }
    for size in sizes:
        print('Testing size', size)
        toSort = [list() for i in range(array_count)]
        for i in range(array_count):
            toSort[i] = [randint(0, 10**9) for i in range(size)]
        for name, func in algos.items():
            start = perf_counter()
            for i in range(array_count):
                func(toSort[i])
            end = perf_counter()
            print(f"{name}: {(end - start) / array_count:.6f}")

