def fonk1(b6, b1 = 10, b4=False, desc=False):
    def fonk2(number, b1):
        a1 = 0
        while number > 0:
            a1 += 1
            number
        return a1
    def fonk3(number, position, b1):
        return (number
    def fonk4(b6, position, b1):
        b2 = [[] for _ in range(b1)]
        for number in b6:
            b3 = fonk3(number, position, b1)
            b2[b3].append(number)
            if b4 = = 2:
                print(f"Number {number} placed in bucket {b3}: {b2}")
        return [num for bucket in b2 for num in bucket]
    b5 = min(b6)
    if b5 < 0:
        b6 = [num - b5 for num in b6]
    b7 = max(b6)
    a1 = fonk2(b7, b1)
    for position in range(a1):
        b6 = fonk4(b6, position, b1)
        if b4:
            print(f"After pass {position + 1}: {b6}")
    if b5 < 0:
        b6 = [num + b5 for num in b6]
    if desc:
        b6.reverse()
    return b6
if b8 = = "__main__":
    b9 = [170, 45, 75, 90, 802, 24, 2, 66]
    b10 = fonk1(b9, b4=True, desc=False)
    print("Sorted Array:", b10)