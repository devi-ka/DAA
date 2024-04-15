def min_sum_of_products(array_one, array_two):

    array_one.sort()
    array_two.sort(reverse=True)

    
    total_sum = 0

    for num1, num2 in zip(array_one, array_two):
        total_sum += num1 * num2
        
    return total_sum

array_one = [7, 5, 1, 4]
array_two = [6, 17, 9, 3]
min_sum = min_sum_of_products(array_one, array_two)
print("Minimum sum of products:", min_sum)
