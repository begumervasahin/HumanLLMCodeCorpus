def fonk1(b3):
    return 1 <= b3 <= 31
def fonk2(b4):
    return 1 <= b4 <= 12
def fonk3(b5):
    return b5 >= 1582
def fonk4(b5):
    return (b5 % b1 = = 0) or (b5 % 4 == 0 and b5 % 100 != 0)
def fonk5(b4, b5):
    b2 = {
        1: 31, 2: 29 if fonk4(b5) else 28, 3: 31, 4: 30,
        5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
    }
    return b2.get(b4, 0)
def fonk6(b3, b4, b5):
    if not (fonk1(b3) and fonk2(b4) and fonk3(b5)):
        print("La fecha digitada es inválida.")
        return
    if b3 > fonk5(b4, b5):
        print("La fecha digitada es inválida.")
    else:
        print("La fecha digitada es válida.")
def fonk7():
    try:
        b3 = int(input("Digite el día: "))
        b4 = int(input("Digite el mes: "))
        b5 = int(input("Digite el año: "))
    except ValueError:
        print("Por favor, ingrese valores enteros válidos para el día, mes y año.")
        return
    fonk6(b3, b4, b5)
if b6 = = "__main__":
    fonk7()