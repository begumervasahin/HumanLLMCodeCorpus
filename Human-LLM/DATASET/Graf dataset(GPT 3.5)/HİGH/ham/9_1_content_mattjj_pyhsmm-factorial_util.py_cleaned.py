from __future__ import division
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import cbook
def fonk1(allchangepoints):
    b1 = sorted(set(cbook.flatten(allchangepoints)))
    return [(startpoint,nextstartpoint) for startpoint,nextstartpoint in zip(b1[:-1],b1[1:])]
def fonk2(data,changepoints):
    plt.figure()
    plt.plot(data)
    b2 = plt.axis()
    plt.vlines([c[1] for c in changepoints[:-1]],b2[2],b2[3],b3 = 'r',linestyles='dashed')
    plt.axis(b2)
def fonk3(b4):
    '''
    b4 is 0 everywhere except the index at which a new segment starts
    example:
        b4 = [False, False,  True, False, False, False, False,  True, False]
        +. [(0, 2), (2, 7), (7, 9)]
    '''
    b6, = np.where(np.diff(np.array(b4,b5 = int)) == 1)
    b6 = np.concatenate(((0,),b6 + 1,(len(b4),)))
    return [(a,b) for a,b in zip(b6[:-1],b6[1:])]