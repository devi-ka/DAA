import random
import timeit
import matplotlib.pyplot as plt

def generate_numbers(n):
    return [random.randint(1, 10000) for _ in range(n)]

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def radix_sort(arr):
    RADIX = 10
    max_length = False
    tmp, placement = -1, 1

    while not max_length:
        max_length = True

        buckets = [list() for _ in range(RADIX)]

        for i in arr:
            tmp = i // placement
            buckets[tmp % RADIX].append(i)
            if max_length and tmp > 0:
                max_length = False

        a = 0
        for b in range(RADIX):
            buck = buckets[b]
            for i in buck:
                arr[a] = i
                a += 1

        placement *= RADIX

def bucket_sort(arr):

    buckets = [[] for _ in range(10)]

    for num in arr:
        index = num // 1000
        buckets[index].append(num)

    for bucket in buckets:
        bucket.sort()

    arr.clear()
    for bucket in buckets:
        arr.extend(bucket)

def plot_results(algorithm_names, execution_times):
    plt.figure(figsize=(10, 6))
    plt.bar(algorithm_names, execution_times, color='skyblue')
    plt.xlabel('Sorting Algorithm')
    plt.ylabel('Time (seconds)')
    plt.title('Comparison of Sorting Algorithms')
    plt.show()

if __name__ == "__main__":

    random_numbers = generate_numbers(1000)

    algorithms = {
        "Bubble Sort": bubble_sort,
        "Selection Sort": selection_sort,
        "Quick Sort": quick_sort,
        "Merge Sort": merge_sort,
        "Radix Sort": radix_sort,
        "Bucket Sort": bucket_sort
    }

    algorithm_names = []
    execution_times = []

    for name, algorithm in algorithms.items():
        start_time = timeit.default_timer()
        algorithm(random_numbers.copy())
        end_time = timeit.default_timer()
        execution_time = end_time - start_time
        algorithm_names.append(name)
        execution_times.append(execution_time)

    plot_results(algorithm_names, execution_times)
