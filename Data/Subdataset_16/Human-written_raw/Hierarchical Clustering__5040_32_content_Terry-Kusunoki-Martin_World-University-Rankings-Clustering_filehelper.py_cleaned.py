b1 = open("timesData.csv", 'r')
b2 = open("universities.points", 'w')
b3 = open("universities.labels", 'w')
b4 = open("metadata.txt", 'w')
a1 = 0
a2 = 0
a3 = 0.0
for line in b1.readlines():
	b5 = line.rstrip().split(',')
	if b5[0] == "world_rank":
		continue
	else:
		b6 = []
		a4 = 0
		for i in range(len(b5)):
			if i <= a4:
				continue
			if '"' in b5[i]:
				b7 = b5[i]
				b8 = i+1
				while '"' not in b5[b8]:
					b8 += 1
				b7 = "".join(b5[i:b8+1]).strip('"')
				b6.append(b7)
				a4 = b8
			else:
				b6.append(b5[i])
		try:
			b9 = int(b6[len(b6)-5])
			b10 = float(b6[len(b6)-4])
			if b9 > a2:
				a2 = b9
			if b10 > a3:
				a3 = b10
		except:
			continue
b4.write("a2: %d\n" % (a2))
b4.write("a3: %b1\n" % (a3))
b1.close()
b1 = open("timesData.csv", 'r')
for line in b1.readlines():
	b5 = line.rstrip().split(',')
	if b5[0] == "world_rank":
		continue
	else:
		b6 = []
		a4 = 0
		for i in range(len(b5)):
			if i <= a4:
				continue
			if '"' in b5[i]:
				b7 = b5[i]
				b8 = i+1
				while '"' not in b5[b8]:
					b8 += 1
				b7 = "".join(b5[i:b8+1]).strip('"')
				b6.append(b7)
				a4 = b8
			else:
				b6.append(b5[i])
		try:
			b9 = float(b6[len(b6)-5])/a2
			b10 = 1.0 - (float(b6[len(b6)-4])/a3)
			b11 = b6[0]
			b12 = float(b6[2])/100
			b13 = b6[len(b6)-6]
			b3.write(b11+"\n")
			try:
				b13 = float(b13)/100
			except:
				b13 = b12
			b2.write(str(b13) +" "+ str(b9) +" "+ str(b10) + "\n")
		except:
			continue
b1.close()
b2.close()
b3.close()
b4.close()