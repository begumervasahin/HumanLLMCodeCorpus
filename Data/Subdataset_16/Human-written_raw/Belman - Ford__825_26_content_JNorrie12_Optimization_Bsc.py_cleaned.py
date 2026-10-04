import numpy as np
b1 = {
	"v_start": {"1_start":0 ,"2_start":0},
	"1_start": {"1_finish":40},
	"2_start": {"2_finish":36},
	"1_finish": {"v_finish":0},
	"2_finish": {"v_finish":0, "1_start":0}
}
def fonk1(v_start):
	return b1.get(v_start)
def fonk2(start, finish):
	b2 = b1.get(start)
	return b2.get(finish)
def fonk3(b1, b3):
	for i in b3:
		for j in fonk1(i):
			b3.append([i])
	print b3
b3 = ['v_start']
fonk3(b1, b3)
def fonk4(b1):
	b3 = []
	b4 = []
	for i in b1['v_start'].keys():
		b3.append([i])
		b4.append(b1['v_start'].get(i))
	for i in b3:
		b5 = i[-1]
		if len(b1[b5].keys()) ==1:
			i.extend(b1[b5].keys())
			b4.extend(b1[b5].values())
		if len(b1[b5].keys())>1:
			for j in b1[b5].keys():
				b3.append([i])
				b3[-1].extend(j)
		for j in b1[i].keys():
			b3.append([])
	return b3 ,b4
print fonk4(b1)