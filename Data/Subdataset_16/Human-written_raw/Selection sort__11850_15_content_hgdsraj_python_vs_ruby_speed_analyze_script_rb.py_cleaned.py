with open('ruby_res.txt') as f:
	b1 = f.readlines()
b2 = []
for i in b1:
	if "real" in i:
		b2.append(i[9:12])
a1 = 0
for i in b2:
	a1 += float(i)/1000
print "The average was"
print a1/40
print "seconds"