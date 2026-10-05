from helper import *
import numpy as np
import random
import copy
import sys
import math
import matplotlib.pyplot as plt
import os
a1 = 200
b1 = './HW
b2 = './HW
def fonk1():
	b3 = read_mat_file(b1, 'data2')
	b4 = read_mat_file(b2, 'b4')
	return b3, b4
def fonk2(ins, center):
	a2 = 0
	for b5 in range(0, len(ins)):
		if b5 = =len(ins):
			break
		a2 += (ins[b5] - center[b5]) ** 2
	a2 = math.sqrt(a2)
	return a2
def fonk3(ins, center):
	a2 = 0
	for b5 in range(0, len(ins)):
		if b5 = =len(ins):
			break
		a2 += abs(ins[b5] - center[b5])
	return a2
def fonk4(ins, center):
	a3 = 0
	a4 = 0
	a5 = 0
	for b5 in range(0, len(ins)):
		if b5 = =len(ins):
			break
		a3 += ins[b5]*center[b5]
		a4 += (ins[b5])**2
		a5 += (center[b5])**2
	if a4 = =0 or a5==0:
		return 1
	return a3/(math.sqrt(a4)*math.sqrt(a5))
def fonk5(cluster):
	if len(cluster)==0:
		return [0, 0, 0, 0]
	b6 = []
	for fieldId in range(len(cluster[0][1])):
		b6.append(0)
		for ins in cluster:
			b6[-1] += ins[1][fieldId]
		b6[-1] /= len(cluster)
	return b6
def fonk6(server_data, b9):
	b7 = {}
	b8 = {}
	for k_num in b9:
		print("For b9 = "+str(k_num)+":")
		b10 = copy.deepcopy(server_data)
		b11 = {}
		b12 = {}
		for b5 in range(k_num):
			b13 = random.randint(0, len(b10)-1)
			b11[b5] = b10[b13]
			b12[b5] = []
			b12[b5].append([b13, b10[b13]])
			del b10[b13]
		for b13, ins in enumerate(b10):
			b14 = sys.maxsize
			a6 = -1
			for center in b11.keys():
				a2 = fonk2(ins, b11[center])
				if a2 < b14:
					b14 = a2
					a6 = center
			b12[a6].append([b13, ins])
		for inter_num in range(a1):
			for a6 in b12.keys():
				b15 = fonk5(b12[a6])
				b11[a6] = [b15[0], b15[1], b15[2], b15[3]]
			for a6 in b12.keys():
				for insId in range(len(b12[a6])):
					if len(b12[a6]) == insId:
						break
					b14 = sys.maxsize
					a7 = -1
					for center in b11.keys():
						a2 = fonk2(b12[a6][insId][1], b11[center])
						if a2 < b14:
							b14 = a2
							a7 = center
					b12[a7].append(b12[a6][insId])
					del b12[a6][insId]
			a8 = 0
			for a6 in b12.keys():
				for insId in range(len(b12[a6])):
					if len(b12[a6]) == insId:
						break
					a8 += (fonk2(b12[a6][insId][1], b11[a6]))**2
			a8 = a8 / len(server_data)
			plt.scatter(inter_num, a8, b16 = 'black')
		print('Cluster Centers: ')
		print(b11)
		b7[k_num] = b11
		b8[k_num] = b12
		a9 = 0
		a10 = 0
		for centerId in b11.keys():
			for val in b12[centerId]:
				a9 += fonk2(val[1], b11[centerId])
		a9 = a9/len(server_data)
		for centerId in b11.keys():
			for val in b12[centerId]:
				for b17 in b11.keys():
					if not b17 = =centerId:
						a10 += fonk2(val[1], b11[b17])
		a10 = a10/len(server_data)
		print("Inner a2: "+str(a9))
		print("Outer a2: "+str(a10))
		for a6 in b12.keys():
			b18 = './Clusters/'+str(k_num)+'_'+str(a6)+'_Kcluster.txt'
			try:
				os.remove(b18)
			except OSError:
				pass
			with open(b18, 'a') as the_file:
				for item in b12[a6]:
					the_file.write(str(item))
					the_file.write('\n')
		plt.show()
	return b7, b8
def fonk7(b3, b4, b9):
	seen_classes, b11 = [], []
	for b13, ins in enumerate(b3):
		if len(b11)==b9:
			break
		if not b4[b13] in seen_classes:
			seen_classes.append(b4[b13])
			b11.append(b13)
	return b11
def fonk8(b20):
	if b20[0]>=b20[1] and b20[0]>=b20[2]:
		return 1
	if b20[1]>=b20[0] and b20[1]>=b20[2]:
		return 2
	if b20[2]>=b20[1] and b20[2]>=b20[0]:
		return 3
def fonk9(b23, b4):
	b19 = {}
	for kVal in b23.keys():
		b19[kVal] = {}
		for classNumber in b23[kVal].keys():
			b20 = [0, 0, 0]
			for ins in b23[kVal][classNumber]:
				b20[b4[ins[0]][0]-1] +=1
			b19[kVal][classNumber] = fonk8(b20)
	return b19
def fonk10(b23, b4, b19):
	b21 = {}
	for kVal in b23.keys():
		all_instances, b22 = 0, 0
		for classNumber in b23[kVal].keys():
			for ins in b23[kVal][classNumber]:
				all_instances += 1
				if not b4[ins[0]][0]==b19[kVal][classNumber]:
					b22 += 1
		b21[kVal] = [all_instances, b22]
	return b21
def fonk11(b3, b4):
	myCenters, b23 = fonk6(b3, [5])
	return b23[5]