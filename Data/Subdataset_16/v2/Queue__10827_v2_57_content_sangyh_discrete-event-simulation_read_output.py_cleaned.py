
import matplotlib.pyplot as plt
def fonk1(b15):
    b1 = []
    b2 = []
    b3 = []
    b4 = []
    b5 = []
    with open(b15, b6 = 'r') as file:
        for line in file.readlines():
            b7 = line.split(' ')
            if line.startswith('PASSENGER ARRIVAL EVENT'):
                b8 = float(b7[-1].strip())
                b1.append(b8)
            elif line.startswith('PASSENGER BOARDING EVENT'):
                b9 = float(b7[-1].strip())
                b2.append(b9)
            elif line.startswith('BUS DEPARTURE EVENT'):
                b10 = float(b7[-1].strip())
                b3.append(b10)
            elif line.startswith('Len of boarded group'):
                b11 = int(b7[-1].strip())
                b4.append(b11)
            elif line.startswith('Len of ToBoard_Que'):
                b12 = int(b7[-1].strip())
                b5.append(b12)
    return (b1, b2,
            b3, b4, b5)
def fonk2(b5):
    plt.plot(range(len(b5)), b5, 'o', b13 = 'Passengers to board queue')
    plt.xlabel('Time')
    plt.ylabel('Queue Length')
    plt.title('Length of To-Board Queue Over Time')
    plt.legend()
    plt.show()
if b14 = = "__main__":
    b15 = "Sample_output-5.txt"
    (b1, b2, b3,
     b4, b5) = fonk1(b15)
    fonk2(b5)