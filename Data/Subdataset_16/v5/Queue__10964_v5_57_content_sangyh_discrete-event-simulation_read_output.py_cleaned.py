
import matplotlib.pyplot as plt
def fonk1(file_path):
    with open(file_path, b1 = 'r') as file:
        b2 = []
        b3 = []
        b4 = []
        b5 = []
        b6 = []
        for line in file.readlines():
            b7 = line.split()
            if line.startswith('PASSENGER ARRIVAL EVENT'):
                b8 = float(b7[-1])
                b2.append(b8)
            elif line.startswith('PASSENGER BOARDING EVENT'):
                b9 = float(b7[-1])
                b3.append(b9)
            elif line.startswith('BUS DEPARTURE EVENT'):
                b10 = float(b7[-1])
                b4.append(b10)
            elif line.startswith('Len of boarded group'):
                b11 = int(b7[-1])
                b5.append(b11)
            elif line.startswith('Len of ToBoard_Que'):
                b12 = int(b7[-1])
                b6.append(b12)
    return b2, b3, b4, b5, b6
def fonk2(queue_lengths):
    plt.plot(range(len(queue_lengths)), queue_lengths, 'o', b13 = 'To-board queue length')
    plt.legend()
    plt.xlabel('Event Index')
    plt.ylabel('Queue Length')
    plt.title('To-Board Queue Length Over Time')
    plt.show()
if b14 = = '__main__':
    b15 = "Sample_output-5.txt"
    b2, b3, b4, b5, b6 = fonk1(b15)
    fonk2(b6)