#input: a string => YES: if contains 'BA' and 'AB' without overlap, else: No
def has_BA_AB(word):
    
    BA_index = word.find('BA')
    AB_index = word.find('AB')
    
    
    if (word.find('BA') < word.find('AB',word.find('BA')+2) ) or ( word.find('AB') < word.find('BA',word.find('AB')+2)) :
        return 1
    else:
        return 0

   
    
input_string = input().upper()
if has_BA_AB(input_string):
    print('YES')
else:
    print('NO')