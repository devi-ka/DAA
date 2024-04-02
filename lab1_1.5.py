def is_palindrome(s):
    if len(s) <= 1:
        return True
    return s[0] == s[-1] and is_palindrome(s[1:-1])

input_string = input("Enter a string: ")
result = is_palindrome(input_string)
if result:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
