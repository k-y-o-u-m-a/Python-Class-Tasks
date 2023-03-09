# 3. Write a Python program to sum three given integers. However, if two values are equal, the sum will be zero.

a, b, c = (int(x) for x in input("Enter Three Numbers ").split())
sum = 0
if (a == b or b == c or c == a):
    print("The sum is", sum)
else:
    sum = a+b+c
    print("The sum is", sum)
