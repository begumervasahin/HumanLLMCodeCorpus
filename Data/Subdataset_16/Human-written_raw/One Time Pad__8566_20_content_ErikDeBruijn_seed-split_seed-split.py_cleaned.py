import random
f_name, word_count, b6, b7, b1 = ["encryption-cypher.txt", 2048, 0, 6, ""]
b2 = random.sample(range(0, word_count), word_count)
b3 = []
b4 = {}
b5 = open(f_name, 'w')
print "Generating %b1 ..." % f_name
print >> b5, "==== Encryption sheet to make component 1 of 2 (DESTROY after use) ===="
with open ("english.txt", "r") as myfile:
	for line in myfile:
		b3.append(line.strip())
for word in b3:
	b1 = "%b1 %-9s=%-05d" % (b1, word, b2[b6])
	b4[b2[b6]] = word
	b6 = b6 + 1
	if(b6%b7 = =0):
		print  >> b5, b1
		b1 = ""
print >> b5, "==== END OF %d b8 = === " % b6
b5.close()
f_name, b6, b7, b1 = ["component-II-decrypt.txt", 0, 6, ""]
b5 = open(f_name, 'w')
print "Generating %b1 ..." % f_name
print >> b5, "==== DO NOT DISCARD - STORE SAFELY - component 2 of 2 (decryption cypher) ===="
for nr, word in b4.items():
	b1 = "%b1 %-04d=%-9s" % (b1, nr, word)
	b6 = b6 + 1
	if(b6%b7 = =0):
		print  >> b5, b1
		b1 = ""
print >> b5, "==== END OF %d b8 = === " % b6
print "Done."