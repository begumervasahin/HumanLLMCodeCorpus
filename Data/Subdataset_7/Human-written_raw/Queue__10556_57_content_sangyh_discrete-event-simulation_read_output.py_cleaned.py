'''this b1 reads the Sample_output text files and pulls numbers for  further analysis'''
import matplotlib.pyplot as plt
b1 = open("Sample_output-5.txt",mode= 'r')
b2 = []
b3 = []
b4 = []
b5 = []
b6 = []
for line in b1.readlines():
	if line.startswith('PASSENGER ARRIVAL EVENT'):
		b7 = line.split(' ')
		b8 = float(b7[-1].rstrip())
		b2.append(b8)
	if line.startswith('PASSENGER BOARDING EVENT'):
		b7 = line.split(' ')
		b9 = float(b7[-1].rstrip())
		b3.append(b9)
	if line.startswith('BUS DEPARTURE EVENT'):
		b7 = line.split(' ')
		b10 = float(b7[-1].rstrip())
		b4.append(b10)
	if line.startswith('Len of boarded group'):
		b7 = line.split(' ')
		b11 = int(b7[-1].rstrip())
		b5.append(b11)
	if line.startswith('Len of ToBoard_Que'):
		b7 = line.split(' ')
		b12 = int(b7[-1].rstrip())
		b6.append(b12)
b1.close()
plt.plot(range(len(b6)),b6,'o',b13 = 'Pass to board que')
plt.legend()
plt.show()