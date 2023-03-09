# 2. Write a program to check if a year is leap year or not.

year = int(input("Enter a Year "))
if (year % 400 == 0 or (year % 100 != 0 and year % 4 == 0)):
    print("The Year {} is a LEAP year".format(year))
else:
    print("The Year {} is not a LEAP year".format(year))
