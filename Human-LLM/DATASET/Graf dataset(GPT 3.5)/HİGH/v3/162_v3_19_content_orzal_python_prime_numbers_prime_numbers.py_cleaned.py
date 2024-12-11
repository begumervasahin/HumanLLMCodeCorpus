def fonk1(num):
    if num < 2:
        return False
    for b1 in range(2, int(num ** 0.5) + 1):
        if num % b1 = = 0:
            return False
    return True
def fonk2(n):
    for b2 in range(2, n):
        if n % b2 = = 0:
            print(f"{n} equals {b2} * {n
            break
if b3 = = "__main__":
    print("Prime numbers from 2 to 99:")
    for num in range(2, 100):
        if fonk1(num):
            print(f"{num} is a prime number")
        else:
            fonk2(num)