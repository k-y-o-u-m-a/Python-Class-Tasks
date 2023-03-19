# 2. A three digit number is called Armstrong number if sum of cube of its digit is equal to number itself.
# Write all Armstrong numbers between 100 to 500.

def armstrong(num):
    num = int(num)
    l = len(str(num))
    sum = 0
    temp = num
    while temp > 0:
        d = temp % 10
        sum += d**l
        temp //= 10
    if (num == sum):
        print(num)


def main():
    print("Armstrong Numbers Between 100 and 500 are:")
    for i in range(100, 501):
        armstrong(i)


if __name__ == "__main__":
    main()
