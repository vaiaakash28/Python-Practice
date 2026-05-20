"""#Armstrong number
n = int(input("Enter a number: "))
sum = 0
temp = n
while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10
if n == sum:
    print(n, "is an Armstrong number")
else:   
    print(n, "is not an Armstrong number")
"""

for i in range (100, 1000):
    order = len(str(i))
    sum = 0
    temp = i
    while temp > 0:
        digit = temp % 10
        sum += digit ** order
        temp //= 10
    if i == sum:
        print(i, "is an Armstrong number")
