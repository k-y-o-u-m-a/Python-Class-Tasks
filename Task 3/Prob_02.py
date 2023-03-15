# 2. Write a Python program to check if a list is empty or not.

list = [int(x) for x in input("Enter items in list ").split()]
if len(list) != 0:
    print("The list is not empty")
else:
    print("The list is empty")
