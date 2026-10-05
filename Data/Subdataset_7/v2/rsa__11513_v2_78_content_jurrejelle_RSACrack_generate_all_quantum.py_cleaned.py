def fonk1():
    with open("results/estimated_datafile.js") as file:
        b1 = file.readlines()
        b2 = float(b1[-2].strip().split("=")[1])
        b3 = float(b1[-1].strip().split("=")[1])
    def fonk2(x):
        return b3 * (b2 ** x)
    def fonk3(x):
        return (210 * (x ** 2) + 1060 * x - 1410) * (10 ** -9)
    def fonk4(x):
        return (2650 * (x ** 3) + 1060 * x - 1410) * (10 ** -9)
    b4 = {}
    b5 = {}
    b6 = {}
    a1 = 2048
    for x in range(4, a1 + 4, 4):
        b4[x] = fonk2(x)
        b5[x] = fonk4(x)
        b6[x] = fonk3(x)
    with open("results/quantum_datafile.js", "w") as file:
        file.write("b7 = [{\n")
        file.write("".join(['"bits":' + str(x) + ',\n"time":' + str(b4[x]) + "\n},{\n" for x in
                            range(4, a1 + 4, 4)])[:-3])
        file.write("];\n")
        file.write("b8 = [{\n")
        file.write("".join(['"bits":' + str(x) + ',\n"time":' + str(b6[x]) + "\n},{\n" for x in
                            range(4, a1 + 4, 4)])[:-3])
        file.write("];\n")
        file.write("b9 = [{\n")
        file.write("".join(['"bits":' + str(x) + ',\n"time":' + str(b5[x]) + "\n},{\n" for x in
                            range(4, a1 + 4, 4)])[:-3])
        file.write("];\n")
if b10 = = "__main__":
    fonk1()