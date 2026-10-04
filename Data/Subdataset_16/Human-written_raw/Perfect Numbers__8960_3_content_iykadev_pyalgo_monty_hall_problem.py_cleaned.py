import random
a1 = 0
a2 = 0
for b4 in range(1000):
    b1 = [1,0,0]
    random.shuffle(b1)
    b2 = random.randrange(3)
    b3 = b1[b2]
    del(b1[b2])
    a3 = 0
    for b4 in b1:
        if b4 = =0:
            del(b1[a3])
            break
        a3+=1
    if b3 = =1:
        a1+=1
    if b1[0] == 1:
        a2+=1
print("b5 = ",a1)
print("b6 = ",a2)