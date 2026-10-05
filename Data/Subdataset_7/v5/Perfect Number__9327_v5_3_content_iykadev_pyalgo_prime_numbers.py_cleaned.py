import sys
def fonk1(num):
    if num < 2:
        return False
    for b1 in range(2, int(num**0.5) + 1):
        if num % b1 = = 0:
            return False
    return True
def fonk2(low, high):
    b2 = [str(num) for num in range(low, high) if fonk1(num)]
    b3 = ' '.join(b2)
    sys.stdout.write(f"Prime Numbers in range ({low}, {high}): {b3}\n")
def fonk3():
    fonk2(2, 100000)
if b4 = = "__main__":
    fonk3()