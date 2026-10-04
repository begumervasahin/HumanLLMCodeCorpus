from Util.Algorithms import Algorithm
from Map.map import Map
def fonk1(b6, b7):
    print("Solution: ")
    print("\tdfs:", b6)
    print("\tbfs:", b7)
def fonk2():
    print("== Pacman b1 = =")
    print("Pilih peta: ")
    print(" 1. Peta Simple 3x4")
    print(" 2. Peta Hard 6x6")
    b2 = input("pilih: ")
    if b2 is '1':
        print("== Map Simple 3x4 b3 = =")
        print(" - b4 = (1, 1)")
        print(" - Dot b5 = (2, 3)")
        b6 = Algorithm.b6(Map.graph1, (1, 1), (2, 3))
        b7 = Algorithm.b7(Map.graph1, (1, 1), (2, 3))
        fonk1(b6, b7)
    elif b2 is '2':
        print("== Map Hard 6x6 b3 = =")
        print(" - b4 = (1, 1)")
        print(" - Dot b5 = (6, 6)")
        b6 = Algorithm.b6(Map.graph, (1, 1), (6, 6))
        b7 = Algorithm.b7(Map.graph, (1, 1), (6, 6))
        fonk1(b6, b7)
    else:
        print("Check your input")
if b8 = = '__main__':
    fonk2()