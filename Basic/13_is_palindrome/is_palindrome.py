#input: a string => if string is a palindrome output: palindrome : not palindrome
def is_palindrome(word):
    first_half = word[:int(len(word)/2)]
    second_half = word[ : (int(len(word)/2)) : -1]
    if first_half == second_half:
        return 1 
    else:
        return 0

input_str = input()
if is_palindrome(input_str):
    print('palindrome')
else:
    print('not palindrome')