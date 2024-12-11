from numpy import *
import matplotlib.pyplot as plt
from pylab import *
x,b1 = loadtxt('dataset.csv', delimiter=',',unpack=True)
b2 = polyfit(x,b1,15)
b3 = stack((x, b1), axis=-1)
b4 = []
for b14,b in b3:
	b4.append([b14, abs(b-polyval(b2,b14))])
b5 = []
for b7 in (list(set(x))):
	b6 = []
	for part_x,part_y in b4:
		if b7 = =part_x:
			b6.append(part_y)
	b5.append([b7,mean(b6)])
b8 = plt.figure(figsize=(18, 9))
b9 = plt.subplot2grid((2, 2), (0, 0), rowspan=1, colspan=2)
plt.title("Value Classifier")
b10 = plt.subplot2grid((2, 2), (1, 0), rowspan=1, colspan=2)
plt.title("Average Distance Classifier")
b11 = []
for b14,b in b3:
	if b>polyval(b2,b14):
		b11.append('
	else:
		b11.append('
b9.scatter(x,b1, b12 = 2,marker='o', c=b11)
b9.plot(x,polyval(b2,x), '
b13 = []
for b14,b in b3:
	for value,max_dist in b5:
		if b14 = =value:
			b15 = max_dist
			if abs(polyval(b2,b14)-b)>max_dist:
				b13.append('r')
			else:
				b13.append('
b10.scatter(x,b1, b12 = 2,marker='o', c=b13)
b10.plot(x,polyval(b2,x), 'k',b16 = '1')
plt.show()