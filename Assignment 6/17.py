# 17. Using range(1,101), make three list, 
# one containing all even numbers
# one containing all odd numbers 
# One containing only prime numbers..


import math


even = []
odd = []
prime = []
for i in range(1,101):
    if(i%2 == 0):
        even.append(i)
    else:
        odd.append(i)

for num in range(2,101):
    if all(num%i!=0 for i in range(2,int(math.sqrt(num))+1)):
       prime.append(num)
       
print("even number:",even)

print("odd number:", odd)

print("Prime number:", prime)