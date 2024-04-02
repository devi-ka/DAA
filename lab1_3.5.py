def merge(arr, temp_arr, left, mid, right):
    inv_count = 0
    i = left  
    j = mid + 1  
    k = left  

    
    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp_arr[k] = arr[i]
            i += 1
        else:
            temp_arr[k] = arr[j]
            j += 1
            inv_count += (mid - i + 1)  
        k += 1

    
    while i <= mid:
        temp_arr[k] = arr[i]
        i += 1
        k += 1

    
    while j <= right:
        temp_arr[k] = arr[j]
        j += 1
        k += 1

    
    for l in range(left, right + 1):
        arr[l] = temp_arr[l]

    return inv_count

def merge_sort(arr, temp_arr, left, right):
    inv_count = 0
    if left < right:
        mid = (left + right) // 2
        inv_count += merge_sort(arr, temp_arr, left, mid)
        inv_count += merge_sort(arr, temp_arr, mid + 1, right)  
        inv_count += merge(arr, temp_arr, left, mid, right)  
    return inv_count

def inversion_count(arr):
    n = len(arr)
    temp_arr = [0] * n  
    return merge_sort(arr, temp_arr, 0, n - 1)


arr = [10, 1, 2, 4, 13, 9, 5]
count = inversion_count(arr)
print("Total count of inversions:", count)
