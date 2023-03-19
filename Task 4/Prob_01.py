# 1. Write a program to find greatest common divisor (GCD) or highest common factor (HCF) of given two numbers.

a = int(input("Enter First Number "))
b = int(input("Enter Second Number "))
mn = min(a, b)
for i in range(mn, 0, -1):
    if a % i == 0:
        if b % i == 0:
            print("HCF is", i)
            break
