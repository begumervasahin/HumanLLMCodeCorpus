import numpy as np
from visual import Plot_press
from scipy.signal import hilbert,welch
import matplotlib.pyplot as plt
class class1(object):
    def fonk1(self, b1,b2):
        self.b1 = b1
        self.b2 = b2
        self.b3 = {}
        self.fonk2(lambda b15: b15)
        self.b4 = []
        self.b5 = []
    def fonk2(self,func):
        '''
        Adding function to the class
        '''
        b6 = 'id'
        self.b3[b6] = func
    def fonk3(self,signal):
        '''
        Remove the mean component from the b1
        and return the flucuation component
        '''
        b7 = signal.mean(axis=0).reshape(1,-1)
        b8 = (signal - np.matmul(
                  np.ones(signal.shape[0]).reshape(-1,1)
                  ,b7))
        return b8
    def fonk4(self,signal):
        ''' Return the covariance of preprocessed b1'''
        b8 = self.fonk3(signal)
        b9 = len(b8)
        b10 = (np.dot(b8.T.conj(),
                    b8)/b9)
        return b10
    def fonk5(self,signal):
        '''
        Return class1 modes using singula value decomposition
        '''
        b10 = self.fonk4(signal)
        u, s, b11 = np.linalg.fonk5(b10, full_matrices=True)
        self.b4 = u[:,0:self.b2]
        self.b5 = s[0:self.b2]
    def fonk6(self):
        '''
        Compute the time_coefficient,or principal components,
        of each modes
        '''
        b12 = self.fonk3(self.b1)
        b13 = np.array(self.b4.T)
        b14 = np.array(b12.T)
        b15 = np.matmul(b13,b14)
        return b15
    def fonk7(self):
        '''
        Plot the frequency transform of time coefficient of Modes
        '''
        b16 = self.fonk6()
        a1 = 700
        b17 = 2**13
        b18 = []
        for i in range(5):
            [freq,spec] = welch(b16[i,:],b19 = b17,nfft=b17,
            b20 = b17/2,b28 = a1)
            b18.append(spec)
        b18 = np.array(b18)
        b21 = []
        for i in range(5):
            b21.append('Mode %i' %(i+1))
        fig, b22 = plt.subplots()
        for i in range(5):
            b22.plot(freq, b18[i,:],b23 = b21[i])
            b22.set_xlim(0,10)
            b22.set_xlabel('freq(Hz)')
            b22.set_ylabel('S(1/Hz)')
            b22.legend(b24 = 'best')
    def fonk8(self):
        '''
        execute class1 and return class1 modes and their corresponding
        eigenvalues
        '''
        self.fonk5(self.b1)
        return self.b4,self.b5
    def fonk9(self):
        '''
        visualizing class1 modes
        '''
        self.fonk2(Plot_press)
        for i in range(self.b2):
            (self.b3['id'](self.b4[:,i],['red','white','blue'],
                          b25 = True,b35=i+1))
        self.fonk7()
class class2(class1):
    def fonk10(self,b1,b2,b26,b27,sampling_freq):
        class1.fonk10(self,b1,b2)
        self.b26 = b26
        self.b27 = b27
        self.b28 = sampling_freq
        self.b29 = []
        self.b30 = []
    def fonk11(self,signal):
        '''
        removing frequencies that lie outside the range of band pass
        '''
        b31 = self.fonk3(signal)
        b32 = len(b31)
        b33 = self.b28/b32
        b34 = (np.linspace(start=-self.b28/2,stop=self.b28/2-b33,
                         b35 = self.b1.shape[0]).T)
        b36 = ((self.b26 < abs(b34)) & (abs(b34) < self.b27)).reshape(-1,1)
        b37 = np.fft.fft(b31,axis=0)
        b38 = (np.fft.fftshift(b37))/b32
        b39 = np.multiply(b36.astype(np.int), b38)
        b40 = np.fft.ifftshift(b39)
        b41 = np.fft.ifft(b40,axis=0)
        b42 = np.real(b41)
        return b42
    def fonk12(self,signal):
        '''
        creating analytic signal using hilbert transform
        this will remove negative frequencies in the filtered signals
        '''
        b43 = self.fonk11(signal)
        b44 = hilbert(b43,axis=0)
        return b44
    def fonk13(self,signal):
        '''
        return class2 modes
        '''
        b44 = self.fonk12(signal)
        b10 = self.fonk4(b44)
        u, s, b11 = np.linalg.fonk5(np.array(b10))
        self.b29 = u[:,0:self.b2]
        self.b30 = s[0:self.b2]
    def fonk14(self):
        '''
        execute class1 and return class1 modes and their corresponding
        eigenvalues
        '''
        self.fonk13(self.b1)
        return self.b29,self.b30
    def fonk15(self, mode_no):
        '''
        visualize the animated movie of class1 mode
        '''
        b45 = self.b29[:,mode_no]
        b46 = b45.reshape(-1,1)
        b47 = np.exp(1j*np.linspace(0,2*np.pi,100)).reshape(1,-1)
        b48 = np.real(b46*b47)
        self.fonk2(Plot_press)
        plt.ion()
        for i in range(100):
            b49 = b48[:,i]
            (self.b3['id'](b49,['red','white','blue'],
                          b25 = False,b35=1))
            plt.pause(0.1)
            plt.clf()