# 6. Take 10 integer inputs from user and store them in a list. Now, copy all the elements in another list but in reverse order.

list = []
list2 = []
print("Enter 10 integers :")
for i in range(0, 10):
    e = int(input())
    list.append(e)
list2 = [list[-i] for i in range(1, len(list)+1)]
# list2 = [i for i in list[::-1]]
print(list2)
