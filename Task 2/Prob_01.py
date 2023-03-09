# 1. Write a Python program to calculate the difference between a given number and 17. If the number is greater than 17, return twice the absolute difference.

num = int(input("Enter a number "))
if num < 17:
    print(int(17-num))
else:
    print(int(2*abs(17-num)))
