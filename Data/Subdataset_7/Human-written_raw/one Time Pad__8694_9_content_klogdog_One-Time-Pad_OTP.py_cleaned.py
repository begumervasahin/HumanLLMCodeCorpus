
b1 = "this is an ultra secret b1:"
import random
b2 = []
b3 = []
b4 = []
b5 = []
b6 = []
a1 = 0
a2 = 0
a3 = 0
b7 = len(b1) + 10000
b8 = {" " : 0, "b2":1,"b":2,"b3":3,"b4":4,"b11":5,"b5":6,"b6":7,"h":8,"i":9,"a1":10,"k":11,"l":12,"a2":13,"n":14,"o":15,"p":16,"q":17,"r":18,"s":19,"t":20,"u":21,"v":22,"w":23,"b13":24,"y":25,"z":26, ":" : 27}
b9 = {0 : " ", 1: 'b2', 2: 'b', 3: 'b3', 4: 'b4', 5: 'b11', 6: 'b5', 7: 'b6', 8: 'h', 9: 'i', 10: 'a1', 11: 'k', 12: 'l', 13: 'a2', 14: 'n', 15: 'o', 16: 'p', 17: 'q', 18: 'r', 19: 's', 20: 't', 21: 'u', 22: 'v', 23: 'w', 24: 'b13', 25: 'y', 26: 'z',27:':'}
for i in range(0,b7):
 b10 = random.randint(0,27)
 b2.append(b10)
print "one time pad"
print b2
for i in b1:
  b3.append(b8[i])
  b11 = b3[a1] + b2[a1]
  if b11 > 28:
    b11 = b11 % 28
  b4.append(b11)
  a1 = a1 + 1
for i in range(len(b1), b7):
    b4.append(b2[i])
print "b1 to number"
print b3
print"encrypted b1"
print b4
a1 = 0
for i in b4:
  b11 = b4[a1] - b2[a1]
  if b11 < 0:
    b11 = b11 + 28
  b5.append(b11)
  a1 = a1 + 1
print "decrypted b1"
print b5
b12 = len(b5)
for i in range(b12):
    b11 = b5[i]
    if b11 = = 27:
        a3 = 1
    if a3 = = 0:
     b6.append(b9[b11])
b13 = "".join(b6)
print b13