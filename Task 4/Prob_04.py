# 4. Write a program to count the total number of digits in a number using a while loop.

num = int(input("Enter a Number: "))
cnt = 0
temp = num
while num:
    num = num//10
    cnt = cnt+1
print("The number {} is a {} digit number".format(temp, cnt))
