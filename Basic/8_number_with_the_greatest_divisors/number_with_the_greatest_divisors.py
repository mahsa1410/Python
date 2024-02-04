#input: 20# numbers => output: the number with the greatest divisors and #of divisors
max_divisors = counter = 0

def divisors_count(x):
    y=0
    for i in range (1 , x+1):
        if x%i == 0:
            y=y+1
    return y 
    
while counter != 5:
    number = int (input())
    divisors = divisors_count(number)
    if max_divisors < divisors:
        max_divisors = divisors
        graetest_nimber = number
    counter = counter +1
print (graetest_nimber , max_divisors)