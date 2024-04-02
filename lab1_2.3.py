import heapq

def k_largest_elements(arr, k):

    min_heap = arr[:k]
    heapq.heapify(min_heap)

    for num in arr[k:]:
        if num > min_heap[0]:
            heapq.heappop(min_heap)
            heapq.heappush(min_heap, num)
    return sorted(min_heap, reverse=True)

arr = [0, 55, 24, 67, 45, 30]
k = 3
result = k_largest_elements(arr, k)
print("The", k, "largest elements in the array are:", result)
