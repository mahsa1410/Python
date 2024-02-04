#input: number of numbers, and then numbers => output: square root of numbers
from math import sqrt
num_list=list()

n = int(input())
for i in range(0,n):
    num_list.append(int(input()))
    
    
for i in num_list:
    print(sqrt(i))