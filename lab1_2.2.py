import heapq

def sorted_lists(arrays):
    min_heap = []
    
    for i, arr in enumerate(arrays):
        if arr:
            heapq.heappush(min_heap, (arr[0], i, 0))
        while min_heap:
            val, arr_index, element_index = heapq.heappop(min_heap)
            print(val)

        if element_index + 1 < len(arrays[arr_index]):
            next_val = arrays[arr_index][element_index + 1]
            heapq.heappush(min_heap, (next_val, arr_index, element_index + 1))


arrays = [
    [10, 20, 30, 40],
    [15, 25, 35],
    [27, 29, 37, 48, 93],
    [32, 33]
]

sorted_lists(arrays)
