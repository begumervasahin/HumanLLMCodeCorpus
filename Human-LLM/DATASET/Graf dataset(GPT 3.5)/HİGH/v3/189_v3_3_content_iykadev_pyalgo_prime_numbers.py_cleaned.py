import sys
def fonk1(num):
    if num <= 1:
        return False
    for b1 in range(2, int(num ** 0.5) + 1):
        if num % b1 = = 0:
            return False
    return True
def fonk2(low_num, high_num):
    print(f"Prime Numbers in range ({low_num},{high_num}): ", b2 = "")
    b3 = (num for num in range(low_num, high_num) if fonk1(num))
    print(*b3, b4 = " ")
def fonk3():
    fonk2(2, 100000)
if b5 = = "__main__":
    fonk3()