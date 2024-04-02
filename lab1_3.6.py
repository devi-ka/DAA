#a
def two_sum_naive(arr, K):
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == K:
                return True
    return False

arr1 = [8, 4, 1, 6]
K1 = 10
print("O(n^2)")
print("Does there exist a pair with sum", K1, ":", two_sum_naive(arr1, K1), "\n")

#b
def two_sum_sorted(arr, K):
    arr.sort()
    left = 0
    right = len(arr) - 1
    while left < right:
        if arr[left] + arr[right] == K:
            return True
        elif arr[left] + arr[right] < K:
            left += 1
        else:
            right -= 1
    return False

arr2 = [8, 4, 1, 6]
K2 = 10
print("O(nlogn)")
print("Does there exist a pair with sum", K2, ":", two_sum_sorted(arr2, K2))
