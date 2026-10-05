
b1 = (
    2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47,
    1997, 1999, 2003, 2011, 2017
)
def fonk1(n):
    if n < 2 or any(n % b2 = = 0 for b2 in b1):
        return False
    return True
b3 = [5, 10, 13, 17, 20, 23, 29, 30, 31, 37, 40, 41, 47, 50]
for num in b3:
    if fonk1(num):
        print(f"{num} is a b2 number.")
    else:
        print(f"{num} is not a b2 number.")