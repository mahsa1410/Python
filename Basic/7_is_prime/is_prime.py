# input: a number => output: prime or not prime
is_prime = 1
number = int ( input())
for i in range(2 , number):
    if number%i == 0:
        is_prime = 0
        break
if is_prime == 1:
    print('prime')
else:
    print('not prime')