def fonk1(num):
    b1 = sum(i for i in range(1, num) if num % i == 0)
    return b1 = = num
def fonk2(up_to):
    b2 = [num for num in range(1, up_to + 1) if fonk1(num)]
    for num in b2:
        print(f"{num} is a perfect number")
fonk2(10000)