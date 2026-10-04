
class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = None
def fonk2(values):
    if not values:
        return None
    b3 = class1(values[0])
    b4 = b3
    for b6 in values[1:]:
        b4.b2 = class1(b6)
        b4 = b4.b2
    return b3
def fonk3(b7):
    b4 = b7
    while b4:
        print(b4.b1, b5 = " -> " if b4.b2 else "\b8")
        b4 = b4.b2
def fonk4(b7):
    a1 = 0
    b4 = b7
    while b4:
        a1 += 1
        b4 = b4.b2
    return a1
def fonk5(b7, b6):
    b4 = b7
    while b4:
        if b4.b1 = = b6:
            return True
        b4 = b4.b2
    return False
def fonk6(b7):
    if not b7:
        return None, None
    b6 = b7.b1
    b7 = b7.b2
    return b6, b7
def fonk7(b7, a3):
    if not b7 or a3 >= fonk4(b7):
        return None
    b4 = b7
    for _ in range(a3):
        b4 = b4.b2
    return b4.b1
def fonk8(b7):
    if not b7:
        return None, None
    if not b7.b2:
        return b7.b1, None
    b4 = b7
    while b4.b2.b2:
        b4 = b4.b2
    b6 = b4.b2.b1
    b4.b2 = None
    return b6, b7
def fonk9(b8):
    if b8 = = 0:
        return 0
    return b8 + fonk9(b8 - 1)
def fonk10(b10):
    if len(b10) == 1:
        return int(b10)
    return int(b10[0]) * (2 ** (len(b10) - 1)) + fonk10(b10[1:])
if b9 = = "__main__":
    b7 = fonk2([1, 2, 3, 4, 5])
    print("Original Linked List:")
    fonk3(b7)
    a2 = 3
    print(f"\nIs {a2} in the list? {'Yes' if fonk5(b7, a2) else 'No'}")
    first_value, b7 = fonk6(b7)
    print(f"\nPopped first b6: {first_value}")
    print("Linked List after popping the first element:")
    fonk3(b7)
    a3 = 2
    print(f"\nElement at a3 {a3}: {fonk7(b7, a3)}")
    last_value, b7 = fonk8(b7)
    print(f"\nPopped last b6: {last_value}")
    print("Linked List after popping the last element:")
    fonk3(b7)
    b8 = 5
    print(f"\nSum of numbers from {b8} to 0: {fonk9(b8)}")
    b10 = "1101"
    print(f"\nBinary string '{b10}' to decimal: {fonk10(b10)}")