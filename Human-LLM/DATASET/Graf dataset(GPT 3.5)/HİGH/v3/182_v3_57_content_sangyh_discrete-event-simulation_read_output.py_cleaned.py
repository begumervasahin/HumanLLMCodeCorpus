import matplotlib.pyplot as plt
def fonk1(b14):
    b1 = []
    b2 = []
    b3 = []
    b4 = []
    b5 = []
    with open(b14, b6 = 'r') as file:
        for line in file:
            b7 = line.split()
            if line.startswith('PASSENGER ARRIVAL EVENT'):
                b8 = float(b7[-1])
                b1.append(b8)
            elif line.startswith('PASSENGER BOARDING EVENT'):
                b9 = float(b7[-1])
                b2.append(b9)
            elif line.startswith('BUS DEPARTURE EVENT'):
                b10 = float(b7[-1])
                b3.append(b10)
            elif line.startswith('Len of boarded group'):
                b11 = int(b7[-1])
                b4.append(b11)
            elif line.startswith('Len of ToBoard_Que'):
                b12 = int(b7[-1])
                b5.append(b12)
    return (b1, b2, b3,
            b4, b5)
def fonk2(data, b13):
    plt.plot(range(len(data)), data, 'o', b13 = b13)
    plt.legend()
    plt.show()
def fonk3():
    b14 = "Sample_output-5.txt"
    (b1, b2, b3,
     b4, b5) = fonk1(b14)
    fonk2(b5, 'Passenger Queue Length')
if b15 = = "__main__":
    fonk3()