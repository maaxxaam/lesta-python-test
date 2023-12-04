from typing import List
from random import randint
from time import perf_counter
from quickSort import quickSort, insertionSort
from radixSort import radixSort

def mainSort(array: List[int]):
    if len(array) < 32:
        insertionSort(array)
    elif len(array) < 512:
        quickSort(array)
    else:
        radixSort(array)

if __name__ == '__main__':
    sizes = [10**2 * i for i in range(1, 11)]
    array_count = 500
    algos = {
            'Quick ': quickSort,
            'Radix ': radixSort,
            'Insert': insertionSort
            }
    for size in sizes:
        print('Testing size', size)
        results = dict()
        toSort = [list() for i in range(array_count)]
        for i in range(array_count):
            toSort[i] = [randint(-10**9, 10**9) for i in range(size)]
        for name, func in algos.items():
            start = perf_counter()
            for i in range(array_count):
                array = toSort[i].copy()
                func(array)
            end = perf_counter()
            print(f"{name}: {(end - start) / array_count:.9f}")
            results[name] = (end - start) / array_count
        print(f"Radix vs Quick: {results['Quick '] / results['Radix ']:.3f}x")

