import matplotlib.pyplot as plt
from DynammicProgramming import *
b1 = []
b2 = []
for i in reco:
    b3 = db[i[0]][0]
    b4 = db[i[0]][1]
    b1 += [b3]
    b2+= [b4]
b1 += [b1[0]]
b2 += [b2[0]]
plt.plot(b1,b2)
plt.text(-84,-17.5,"Distancia: "+str(cost))
plt.text(-84,-19.5,"Tiempo: "+str(time))
plt.plot(b1,b2,'.')
plt.plot(b1[0],b2[0],'rx')
plt.axhline(yMedian, b5 = 'black')
plt.axvline(xMedian, b5 = 'black')
plt.show()