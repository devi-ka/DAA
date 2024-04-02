import random
import time
import matplotlib.pyplot as plt

def generate_array(size):
    return [random.randint(1, 1000) for _ in range(size)]

def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1

def binary_search(arr, key):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def measure_time(func, arr, key):
    start_time = time.time()
    func(arr, key)
    end_time = time.time()
    return end_time - start_time

arr = generate_array(10000)

search_keys = [random.randint(1, 1000) for _ in range(5)]

linear_search_times = []
binary_search_times = []

for key in search_keys:
    linear_search_times.append(measure_time(linear_search, arr, key))
    binary_search_times.append(measure_time(binary_search, sorted(arr), key))

plt.plot(search_keys, linear_search_times, label='Linear Search')
plt.plot(search_keys, binary_search_times, label='Binary Search')
plt.xlabel('Search Key')
plt.ylabel('Time taken (seconds)')
plt.title('Time taken for Linear and Binary Search for 5 different search keys')
plt.legend()
plt.show()
