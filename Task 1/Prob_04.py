# 4.Display float number with 2 decimal places using print().

num = float(input("Enter a number "))
print("%.2f" % num)             # Method 1
print("{0:.2f}".format(num))    # Method 2
print(round(num, 2))            # Method 3
