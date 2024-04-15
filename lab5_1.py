def candies(n, arr):
    candies = [1] * n

    for i in range(1, n):
        if arr[i] > arr[i-1]:
            candies[i] = candies[i-1] + 1

    for i in range(n-2, -1, -1):
        if arr[i] > arr[i+1]:
            candies[i] = max(candies[i], candies[i+1] + 1)

    total_candies = sum(candies)
    
    return total_candies

n = int(input("Enter the number of children in the class: "))
arr = []
print("Enter the ratings of each student:")
for _ in range(n):
    rating = int(input())
    arr.append(rating)

print("Minimum number of candies Alice must buy:", candies(n, arr))
