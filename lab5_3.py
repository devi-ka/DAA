def pylons(k, arr):
    n = len(arr)
    count = 0
    i = 0
    
    while i < n:
        j = min(i + k - 1, n - 1)
        while j >= i - k + 1 and arr[j] == 0:
            j -= 1
        
        if j < i - k + 1:
            return -1
        
        count += 1
        i = j + k
    
    return count

# Sample Input
n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Output
print(pylons(k, arr))
