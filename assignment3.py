import time
import random
import sys

sys.setrecursionlimit(20000)


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1


def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)


def partition(arr, low, high):
    pivot_index = random.randint(low, high)
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]

    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i + 1


def measure_time(func, arr):
    temp = arr.copy()

    start = time.perf_counter()

    if func == quick_sort:
        if len(temp) > 0:
            func(temp, 0, len(temp)-1)
    else:
        func(temp)

    end = time.perf_counter()

    return round(end - start, 6)


def generate_data(size):
    data = [random.randint(1, 100000) for _ in range(size)]
    return data, sorted(data), sorted(data, reverse=True)


if __name__ == "__main__":

    # correctness check
    test = [5, 2, 9, 1, 5, 6]
    quick_sort(test, 0, len(test)-1)
    print("Correctness:", test)

    sizes = [1000, 5000]

    print("\nSize | Type | Insertion | Merge | Quick")

    for size in sizes:
        r, s, rev = generate_data(size)

        for name, data in [("Random", r), ("Sorted", s), ("Reverse", rev)]:
            t1 = measure_time(insertion_sort, data)
            t2 = measure_time(merge_sort, data)
            t3 = measure_time(quick_sort, data)

            print(f"{size} | {name} | {t1}s | {t2}s | {t3}s")