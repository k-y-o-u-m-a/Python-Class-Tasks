# 5. Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.

list = [x for x in input("Enter the list items : ").split()]
pos = [0, 4, 5]
list = [element for (index, element) in enumerate(list) if index not in pos]
print(list)
