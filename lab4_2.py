def maximize_sum(arr):

    arr.sort()

    total_sum = 0

    for i, num in enumerate(arr):
        total_sum += num * i
        
    return total_sum

arr = [2, 5, 3, 4, 0]
maximized_sum = maximize_sum(arr)
print("Maximum sum:", maximized_sum)
