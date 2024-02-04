#input: a string => output:
#Delete vowels
#Print a dot before each silent letter
#Write all the remaining silent letters in lowercase
def delete_vowels(x):
    vowels = {'a','e','i','o','u'}
    for i in vowels:
        if i in x :
            x = x.replace(i , '')
    return x

def insert_dot(x):
    y=''
    for i in x:
        y = y +'.'+i
    return y

input_string = delete_vowels( input().lower() )
input_string = insert_dot(input_string)
print(input_string)