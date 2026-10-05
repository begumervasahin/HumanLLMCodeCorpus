import time
import random
def fonk1(b3):
    b1 = time.time()
    b2 = False
    if len(b3)==0:
      b3 = []
      return b3
    while not b2 :
        for i,val in enumerate(b3):
            for j,val1 in enumerate(b3):
                if (b3[i]>b3[j]):
                    b3[i],b3[j] = b3[j],b3[i]
                    b2 = True
    return b3
try:
    b4 = input().split(' ')
    b4 = [int(x) for x in b4]
    fonk1(b4)
except:
    print("[]")
fonk1(b4)