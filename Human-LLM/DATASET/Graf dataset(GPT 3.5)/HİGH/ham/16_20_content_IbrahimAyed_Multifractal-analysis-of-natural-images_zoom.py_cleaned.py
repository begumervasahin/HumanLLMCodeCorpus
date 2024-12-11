
import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate
def fonk1(l,L,b26,b1 = 1.0,Ymax=1.0):
    b2 = l
    b3 = 1.0*L
    b4 = (1.0/(b2**2)-1)
    b5 = (1.0/(b3**2)-1)
    b6 = (2.0/np.pi)*(b4-b5)*(b1+1)*(Ymax+1)
    b7 = np.random.poisson(b6)
    b8 = (b4-b5)*np.random.uniform(size=b7)+b5
    b9 = 1.0/np.sqrt(b4-b8+b5)
    b10 = -0.5 + np.random.uniform(size=b7) * (b1+1)
    b11 = -0.5 + np.random.uniform(size=b7) * (Ymax+1)
    b12 = np.sqrt(0.08)
    b13 = -0.5*0.08
    b14 = np.random.randn(b7)*b12+b13
    b15 = np.linspace(0, b1, b26)
    b16 = np.linspace(0, Ymax, b26)
    X, b17 = np.meshgrid(b15, b16)
    b18 = np.zeros((b26,b26))
    for i in range(b7):
        b19 = ((((X-b10[i])/b9[i])**2+((b17-b11[i])/b9[i])**2)<0.25)
        b18[b19] = b18[b19] + b14[i]
    b20 = np.exp(b18)
    b21 = (b2/b3)**(np.exp(b13+0.5*b12**2)-1)
    return b20/b21
def fonk2(l,b26,b1 = 1.0,Ymax=1.0):
    return fonk1(l,1.0,b26,b1,Ymax)
def fonk3(Im,b26,b1,Ymax):
    b15 = np.linspace(0, b1, b26)
    b16 = np.linspace(0, Ymax, b26)
    X, b17 = np.meshgrid(b15, b16)
    b22 = np.linspace(0, b1, b26*2)
    b23 = np.linspace(0, Ymax, b26*2)
    X_new, b24 = np.meshgrid(b22, b23)
    b25 = interpolate.interp2d(b15, b16, Im)
    return b25(b22,b23)
def fonk4(Qr,a2):
    b26 = Qr.shape[0]
    b15 = np.concatenate((np.arange(0,1+b26/2),np.arange(-b26/2+1,0)))
    U,b27 = np.meshgrid(b15,b15)
    b28 = U**2+b27**2
    b28[0,0] = 1.0
    return np.real(np.fft.ifft2(np.fft.fft2(Qr)/(b28**a2)))
def fonk5(Qr,a2):
    b26 = Qr.shape[0]
    b15 = np.concatenate((np.arange(0,1+b26/2),np.arange(-b26/2+1,0)))
    U,b27 = np.meshgrid(b15,b15)
    b28 = U**2+b27**2
    b28[0,0] = 1.0
    return np.real(np.fft.ifft2(np.fft.fft2(Qr)*(b28**a2)))
def fonk6(b38,Iold):
    b29 = b38.shape[0]
    b26 = Iold.shape[0]
    if((b38.shape[1]!=b29)or(Iold.shape[1]!=b26)or((b29/b26)!=2**(int(np.log2(b29/b26))))):
        print("Error size of images")
        return
    for i in range(b26):
        for j in range(b26):
            b30 = Iold[i,j]
            b38[2*i:2*(i+1),2*j:2*(j+1)] = b30*b38[2*i:2*(i+1),2*j:2*(j+1)]/np.sum(b38[2*i:2*(i+1),2*j:2*(j+1)])
    return b38
def fonk7(Im,a2,a1):
    b26 = Im.shape[0]
    b1 = 1.0
    b31 = 1.0/b26
    b32 = fonk3(Im,b26,b1,b1)
    plt.figure()
    plt.imshow(b32,b33 = 'magma')
    plt.plot()
    b34 = fonk5(b32,a2)
    b35 = fonk1(0.5*b31,b31,2*b26,b1,b1)
    b36 = b34*b35+a1*1*(b35-b35.mean())
    b37 = Im.mean() + fonk4(b36,a2)
    b37 = np.maximum(b37,np.zeros_like(b37))
    b38 = fonk6(b37,Im)
    return b38
b1 = 1.0
b26 = 32
b20 = fonk2(1.0/b26,b26,b1,b1)
a1 = 8
a2 = 0.7
a3 = 23
b39 = a3+a1*fonk4(b20-b20.mean(),a2)
plt.figure()
plt.imshow(b39,b33 = 'magma')
plt.plot()
b40 = fonk7(b39,a2,a1)
plt.figure()
plt.imshow(b40,b33 = 'magma')
plt.plot()
b41 = fonk7(b40,a2,a1)
plt.figure()
plt.imshow(b41,b33 = 'magma')
plt.plot()
b42 = fonk7(b41,a2,a1)
plt.figure()
plt.imshow(b42,b33 = 'magma')
plt.plot()
b43 = fonk7(b42,a2,a1)
plt.figure()
plt.imshow(b43,b33 = 'magma')
plt.plot()
b44 = fonk7(b43,a2,a1)
plt.figure()
plt.imshow(b44,b33 = 'magma')
plt.plot()
a4 = 8
b45 = b39[a4:a4+16,a4:a4+16]
plt.figure()
plt.imshow(b45,b33 = 'magma')
plt.plot()
b46 = b41[a4*4:(a4+16)*4,a4*4:(a4+16)*4]
plt.figure()
plt.imshow(b46,b33 = 'magma')
plt.plot()
b46 = b42[a4*8:(a4+16)*8,a4*8:(a4+16)*8]
plt.figure()
plt.imshow(b46,b33 = 'magma')
plt.plot()
b46 = b43[a4*16:(a4+16)*16,a4*16:(a4+16)*16]
plt.figure()
plt.imshow(b46,b33 = 'magma')
plt.plot()