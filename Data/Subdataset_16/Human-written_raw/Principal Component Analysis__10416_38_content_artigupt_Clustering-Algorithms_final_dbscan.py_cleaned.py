
from cluster import *
from pylab import *
class class1:
    b1 = []
    a1 = 0
    b2 = []
    b3 = []
    b4 = []
    def fonk1(D,eps,MinPts):
        b1 = D
        a2 = -1
        b5 = None
        for i in D:
            if i not in b2:
                b2.append(point)
                b6 = fonk3(point,eps)
                if len(b6) < MinPts:
                    b5.addPoint(point)
                else:
                    b7 = 'Cluster'+str(a1);
                    a2 = cluster(b7)
                    a1+=1;
                    fonk2(point,b6,a2,eps,MinPts)
    def fonk2(point,b6,a2,eps,MinPts):
        a2.addPoint(point)
        for p in b6:
            if p not in b2:
                b2.append(p)
                b8 = fonk3(p,eps)
                if len(b8) >= MinPts:
                    for n in b8:
                        if n not in b6:
                            b6.append(n)
            for c in b4:
                if not c.has(p):
                    if not a2.has(p):
                        a2.addPoint(p)
            if len(b4) == 0:
                if not a2.has(p):
                    a2.addPoint(p)
        b4.append(a2)
    def fonk3(point,eps):
        b9 = []
        for d in b1:
            if (((d[0]-point[0])**2 + (d[1] - point[1])**2)**0.5)<=eps:
                b9.append(d)
        return b9
        fonk1(points,0.3,10)