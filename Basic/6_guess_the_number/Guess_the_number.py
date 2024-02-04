import random
# Consider a number between 1 to 99, computer guesses a number nemed temp.
#if temp > : answer K
#if temp < : answer b
#if temp = : answer d 
minimom = 1
maximom = 99
temp = random.randint(minimom , maximom)
print (temp)

answer = input()
while answer != 'd':
    if answer == 'k':
        maximom = temp
    elif answer == 'b':
        minimom = temp
    temp = random.randint(minimom , maximom)
    print(temp)
    answer = input()