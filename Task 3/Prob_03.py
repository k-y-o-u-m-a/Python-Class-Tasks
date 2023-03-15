# 3. Write a Python function that takes two lists and returns True if they have at least one common member.

l1 = [int(x) for x in input("Enter items in list 1 ").split()]
l2 = [int(x) for x in input("Enter items in list 2 ").split()]
ans = False
for x in l1:
    for y in l2:
        if x == y:
            ans = True
            break
if ans == True:
    print("Atleast One Common Element is Present")
else:
    print("No Common Element Present")
