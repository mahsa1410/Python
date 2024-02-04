#input : a string => find 'hello' pattern at input string , output: yes or no
def is_pattern_in(in_string):
    pattern = 'hello'
    temp =''
    prev_index = 0
    for i in pattern:
        if in_string.find(i , prev_index+1) > 0:
            temp = temp + in_string[in_string.find(i , prev_index+1)]
            prev_index = in_string.find(i , prev_index+1)
        else:
            return 0
    #print (temp)
    if temp == pattern:
        return 1
            
    
input_string = input()
if is_pattern_in(input_string):
    print('yes')
else:
    print('no')