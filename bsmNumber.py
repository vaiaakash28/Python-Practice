"""a = 10
b = 20
c = 15
biggest = max(a, b, c)
print("The biggest number is:", biggest)

numbers = [a, b, c]
biggest = max(numbers)
print("The biggest number is:", biggest)

a = input("Enter the first number: ")
b = input("Enter the second number: ")
c = input("Enter the third number: ")

numbers = [a, b, c]
biggest = max(numbers)
print("The biggest number is:", biggest)"""


""" 

if a > b:
    if a > c:
        biggest = a
    else:
        biggest = c
else:
    if b > c:
        biggest = b
    else:  
        biggest = c 
"""

"""
if a > b:
    x = a 

else:
    x = b 
if x > c:
    big = x 
else: 
    big = c
"""


a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

#maximum number
big = a
if b > big:
    big = b
if c > big:
    big = c
print("The biggest number is:", big)

#minimum number 
min = a 
if b < min:
    min = b
if c < min:
    min = c

print("The smallest number is:", min)

#middle number
mid = a + b + c - big - min
print("The middle number is:", mid)


for i in range(100,200):
    print(i)
