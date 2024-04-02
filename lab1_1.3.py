def string_to_integer(s):
    if len(s) == 0:
        return 0
    
    return string_to_integer(s[:-1]) * 10 + int(s[-1])

input_string = input("Enter a string of digits: ")
result = string_to_integer(input_string)
formatted_result = "{:,}".format(result)
print("The integer representation is:", formatted_result)
