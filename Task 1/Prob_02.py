# 2. Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.

num = int(input("Enter a Number "))
val = num+num*num+num**3
print("The required value is", val)
