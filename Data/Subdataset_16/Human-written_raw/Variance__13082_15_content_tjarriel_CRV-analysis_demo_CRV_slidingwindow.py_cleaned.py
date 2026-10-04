
import cv2
import numpy as np
from numpy import *
from rivamap import singularity_index, georef
import glob, os
import matplotlib.pyplot as plt
for x in range(15,60,5):
    b1 = '/home/engrla/rivamap/SIESD related/SlidingWindow/demo_PSIs'
    b2 = sorted(glob.glob(b1 + '*/*.TIF'))
    b3 = x
    b4 = (len(b2)-b3)+1
    print ('number of singularity index images: ')
    print(len(b2))
    print ('number of windows: ')
    print(b4)
    print ('step size: ')
    print(x)
    b5 = cv2.imread(b2[0], cv2.IMREAD_UNCHANGED)
    b6 = np.zeros((b3, b5.shape[0], b5.shape[1]), dtype='float32')
    b7 = []
    b8 = list(range(0,b4))
    for i in range(0,b4,1):
        for j in range(i,i+b3):
            b9 = cv2.imread(b2[j], cv2.IMREAD_UNCHANGED)
            b6[j-i,:,:] = b9
        b10 = np.var(b6,axis=0)
        b11 = np.mean(b10)
        print('window '+str(i))
        b7.append(b11)
        b6 = np.zeros((b3, b5.shape[0], b5.shape[1]), dtype='float32')
    plt.scatter(b8,b7)
    plt.xlabel('window number')
    plt.ylabel('average CRV for window images')
    plt.savefig(os.path.join("demo_slidingwindow_"+str(x)+".TIF"))
    plt.savefig(os.path.join("demo_slidingwindow_"+str(x)+".eps"), b12 = 'eps')
    plt.close('all')
print('completed')