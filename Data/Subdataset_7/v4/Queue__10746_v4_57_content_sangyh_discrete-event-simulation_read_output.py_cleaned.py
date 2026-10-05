import matplotlib.pyplot as plt
with open("Sample_output-5.txt", b1 = 'r') as file:
    b2 = []
    b3 = []
    b4 = []
    b5 = []
    b6 = []
    for line in file.readlines():
        if line.startswith('PASSENGER ARRIVAL EVENT'):
            b7 = line.split(' ')
            b8 = float(b7[-1].rstrip())
            b2.append(b8)
        elif line.startswith('PASSENGER BOARDING EVENT'):
            b7 = line.split(' ')
            b9 = float(b7[-1].rstrip())
            b3.append(b9)
        elif line.startswith('BUS DEPARTURE EVENT'):
            b7 = line.split(' ')
            b10 = float(b7[-1].rstrip())
            b4.append(b10)
        elif line.startswith('Len of boarded group'):
            b7 = line.split(' ')
            b11 = int(b7[-1].rstrip())
            b5.append(b11)
        elif line.startswith('Len of ToBoard_Que'):
            b7 = line.split(' ')
            b12 = int(b7[-1].rstrip())
            b6.append(b12)
plt.plot(range(len(b6)), b6, 'o', b13 = 'Pass to board que')
plt.legend()
plt.show()