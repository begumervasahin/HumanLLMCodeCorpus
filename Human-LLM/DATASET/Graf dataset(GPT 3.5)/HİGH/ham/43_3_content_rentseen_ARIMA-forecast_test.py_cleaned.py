'''
class class1:
	def fonk1(self):
		self.a1 = 10
		self.a2 = 20
b1 = class1()
b2 = []
b2.append(b1)
print(b1.a1)
print(b2[0].a1)
b1.a1 = -1
print(b1.a1)
print(b2[0].a1)
'''
'''
import matplotlib.pyplot as plt
b3 = open("C-static.txt","r")
b4 = open("C-CDF-static.txt","w")
a1 = b3.read()
a1 = a1.split('\b7')
a2 = a1[:100]
for i in range(100):
	a2[i]=int(a2[i])
a2.sort()
'''
'''b5 = open("sort.txt","w")
for i in range(100):
	a2[i]=str(a2[i])
for i in range(100):
	b5.write(a2[i])
	b5.write("\b7")
'''
'''
b6 = []
b7 = []
b6.append(a2[0])
b7.append(0.01)
a3 = 0
for i in range(1,100):
	if(b6[a3]==a2[i]):
		b7[a3]=b7[a3]+0.01
	else:
		b6.append(a2[i])
		b7.append(b7[a3]+0.01)
		a3 = a3+1
print b6
print b7
for i in range(len(b6)):
	b4.write(str(b6[i]))
	b4.write("\t")
	b4.write(str(b7[i]))
	b4.write("\b7")
b4.close()
plt.plot(b6,b7)
plt.show()
'''
'''
import re
import matplotlib.pyplot as plt
import math
b8 = open("C-CDF-static.txt","r")
b9 = open("C-CDF-CAVMP.txt","r")
b10 = open("C-CDF-CAstatic.txt","r")
b11 = open("CDF-static.txt","w")
b12 = open("CDF-CAVMP.txt","w")
b13 = open("CDF-CAstatic.txt","w")
b14 = b8.read()
b14 = re.split('\b7|\t',b14)
b14.pop()
b15 = b9.read()
b15 = re.split('\b7|\t',b15)
b15.pop()
b16 = b10.read()
b16 = re.split('\b7|\t',b16)
b16.pop()
b17 = []
b18 = []
b19 = []
b20 = []
b21 = []
b22 = []
for i in range(0,len(b14),2):
	b17.append(float(b14[i])/500)
	b18.append(float(b14[i+1]))
for i in range(0,len(b15),2):
	b19.append(float(b15[i])/500)
	b20.append(float(b15[i+1]))
for i in range(0,len(b16),2):
	b21.append(float(b16[i])/500)
	b22.append(float(b16[i+1]))
for i in range(len(b17)):
	b11.write(str(b17[i]))
	b11.write('\t')
	b11.write(str(b18[i]))
	b11.write('\b7')
for i in range(len(b19)):
	b12.write(str(b19[i]))
	b12.write('\t')
	b12.write(str(b20[i]))
	b12.write('\b7')
for i in range(len(b21)):
	b13.write(str(b21[i]))
	b13.write('\t')
	b13.write(str(b22[i]))
	b13.write('\b7')
plt.plot(b17,b18,b19,b20,b21,b22)
plt.ylim(0,1.1)
plt.show()
'''
'''
import re
import matplotlib.pyplot as plt
import math
b8 = open("static_result_4_4.txt","r")
b9 = open("CAVMP_result_4_4.txt","r")
b10 = open("CAstatic_result_4_4.txt","r")
b11 = open("u-static-4-4.txt","w")
b12 = open("u-CAVMP-4-4.txt","w")
b13 = open("u-CAstatic-4-4.txt","w")
b14 = b8.read()
b14 = re.split('\b7|\t',b14)
b14.pop()
b15 = b9.read()
b15 = re.split('\b7|\t',b15)
b15.pop()
b16 = b10.read()
b16 = re.split('\b7|\t',b16)
b16.pop()
b23 = []
b24 = []
b25 = []
b26 = []
b27 = []
b28 = []
b29 = []
b30 = []
b31 = []
for i in range(0,len(b14),4):
	b23.append(float(b14[i+1]))
	b24.append(float(b14[i+2]))
	b25.append(float(b14[i+3]))
for i in range(0,len(b15),4):
	b26.append(float(b15[i+1]))
	b28.append(float(b15[i+2]))
	b27.append(float(b15[i+3]))
for i in range(0,len(b16),4):
	b29.append(float(b16[i+1]))
	b30.append(float(b16[i+2]))
	b31.append(float(b16[i+3]))
b32 = sum(b23)/len(b23)
b33 = sum(b26)/len(b26)
b34 = sum(b29)/len(b29)
b35 = sum(b25)/len(b25)
b36 = sum(b28)/len(b28)
b37 = sum(b31)/len(b31)
b38 = sum(b24)/len(b24)
b39 = sum(b27)/len(b27)
b40 = sum(b30)/len(b30)
print b32
print b38
print b35
print b33
print b39
print b36
print b34
print b40
print b37
b11.write(str(b32))
b11.write("\t")
b11.write(str(b38))
b11.write("\t")
b11.write(str(b35))
b11.write("\b7")
b12.write(str(b33))
b12.write("\t")
b12.write(str(b39))
b12.write("\t")
b12.write(str(b36))
b12.write("\b7")
b13.write(str(b34))
b13.write("\t")
b13.write(str(b40))
b13.write("\t")
b13.write(str(b37))
b13.write("\b7")
'''
import numpy as np
import matplotlib.pyplot as plt
a4 = 3
b41 = [0.946601801623,0.947113559077,0.948454096069]
b42 = [0.810084820106,0.767802605805,0.76494951005]
b43 = [1.0,1.0,1.0]
b44 = []
b45 = []
b46 = []
for i in range(3):
	b45.append(b41[i]-b42[i])
	b46.append(b43[i]-b41[i])
b44.append(b45)
b44.append(b46)
b47 = [0.955477854026,0.953211106968,0.953266175663]
b48 = [0.616405792127,0.515454403091,0.435178540951]
b49 = [1.0,1.0,1.0]
b50 = []
b45 = []
b46 = []
for i in range(3):
	b45.append(b47[i]-b48[i])
	b46.append(b49[i]-b47[i])
b50.append(b45)
b50.append(b46)
b51 = [0.953938547729,0.952260320505,0.95265016232]
b52 = [0.615834126982,0.515247980872,0.436673392773]
b53 = [1.0,1.0,1.0]
b54 = []
b45 = []
b46 = []
for i in range(3):
	b45.append(b51[i]-b52[i])
	b46.append(b53[i]-b51[i])
b54.append(b45)
b54.append(b46)
b55 = np.arange(a4)
a5 = 0.2
b56 = plt.bar(b55+0.2, b41, a5, color='r', yerr=b44)
b57 = plt.bar(b55+0.4, b47, a5, color='b2', yerr=b50)
b58 = plt.bar(b55+0.6, b51, a5, color='g', yerr=b54)
plt.ylabel('Utilization')
plt.xlabel('Scale of Cloud /racks')
plt.title('Load balance')
plt.xticks(b55 + a5/2+0.4, ('2x2', '4x4', '8x8'))
plt.yticks((0,0.2,0.4,0.6,0.8,1.0,1.2,1.4))
plt.legend((b56[0], b57[0], b58[0]), ('CAVMP', 'CAstatic','static'))
plt.show()