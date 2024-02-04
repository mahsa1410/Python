#input: a string in combinentional small and capital letters : ouput: if capital# > small# print the string upper
def how_meny_capital(input_str):
    captal_count = 0
    for letter in input_str:
        if letter.isupper():
            captal_count = captal_count +1
    return captal_count

word = input()
captal_count = how_meny_capital(word)
if len(word) - captal_count < captal_count:
    print(word.upper())
else:
    print(word.lower())