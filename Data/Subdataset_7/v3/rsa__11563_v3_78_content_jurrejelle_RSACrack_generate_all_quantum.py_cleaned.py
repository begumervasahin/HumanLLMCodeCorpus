def fonk1(file_path):
    with open(file_path) as file:
        b1 = file.readlines()
        b2 = float(b1[-2].strip().split("=")[1])
        b3 = float(b1[-1].strip().split("=")[1])
    return b2, b3
def fonk2(b2, b3, x):
    return b3 * (b2 ** x)
def fonk3(x):
    return (210 * (x ** 2) + 1060 * x - 1410) * (10 ** -9)
def fonk4(x):
    return (2650 * (x ** 3) + 1060 * x - 1410) * (10 ** -9)
def fonk5(file_path, b9, b10, b11):
    with open(file_path, "w") as file:
        file.write("b4 = [{\n")
        file.write("".join(['"bits":' + str(x) + ',\n"time":' + str(b9[x]) + "\n},{\n" for x in range(4, highest + 4, 4)])[:-3])
        file.write("];\n")
        file.write("b5 = [{\n")
        file.write("".join(['"bits":' + str(x) + ',\n"time":' + str(b10[x]) + "\n},{\n" for x in range(4, highest + 4, 4)])[:-3])
        file.write("];\n")
        file.write("b6 = [{\n")
        file.write("".join(['"bits":' + str(x) + ',\n"time":' + str(b11[x]) + "\n},{\n" for x in range(4, highest + 4, 4)])[:-3])
        file.write("];\n")
def fonk6():
    b7 = "results/estimated_datafile.js"
    b8 = "results/quantum_datafile.js"
    a1 = 2048
    b2, b3 = fonk1(b7)
    b9 = {x: fonk2(b2, b3, x) for x in range(4, a1 + 4, 4)}
    b10 = {x: fonk3(x) for x in range(4, a1 + 4, 4)}
    b11 = {x: fonk4(x) for x in range(4, a1 + 4, 4)}
    fonk5(b8, b9, b10, b11)
if b12 = = "__main__":
    fonk6()