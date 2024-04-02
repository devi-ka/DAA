def pair_sum(arr, target):
    num_indices = {}
    for i, num in enumerate(arr):
        complement = target - num
        if complement in num_indices:
            return (num_indices[complement], i)
        num_indices[num] = i
    return None
"""
num = [8, 7, 2, 5, 3, 1]
target = 10"""
num= [5, 2, 6, 8, 1, 9]
target= 12
pair_indices = pair_sum(num, target)
if pair_indices:
    print("Pair found at indices:", pair_indices)
    print("Values are:", num[pair_indices[0]], "and", num[pair_indices[1]])
else:
    print("No pair found ")
