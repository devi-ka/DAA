def swapped_elements(arr):
    n = len(arr)
    first, second = None, None
    
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            if first is None:
                first = i
            second = i + 1
            
    return first, second

def sort_array(arr):
    first, second = swapped_elements(arr)
    
    if first is None or second is None:
        return arr
    
    arr[first], arr[second] = arr[second], arr[first]
    
    return arr

arr = [3, 8, 6, 7, 5, 9] or [3, 5, 6, 9, 8, 7] or [3, 5, 7, 6, 8, 9]
sorted_arr = sort_array(arr)
print("Sorted array:", sorted_arr)
