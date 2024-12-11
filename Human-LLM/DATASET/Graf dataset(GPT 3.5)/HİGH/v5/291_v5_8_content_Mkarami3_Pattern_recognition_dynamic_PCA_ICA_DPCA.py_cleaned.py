import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import hilbert, welch
from visual import Plot_press
class class1:
    def fonk1(self, b1, b2):
        self.b1 = b1
        self.b2 = b2
        self.b3 = {}
        self.fonk2(lambda x: x)
        self.b4 = []
        self.b5 = []
    def fonk2(self, func):
        '''Add a function to the class.'''
        self.b3['id'] = func
    def fonk3(self, signal):
        '''Remove the mean component from the b1 and return the fluctuation component.'''
        b6 = np.mean(signal, axis=0).reshape(1, -1)
        b7 = signal - np.dot(np.ones((signal.shape[0], 1)), b6)
        return b7
    def fonk4(self, signal):
        '''Return the covariance of the preprocessed b1.'''
        b7 = self.fonk3(signal)
        b8 = len(b7)
        b9 = np.dot(b7.T.conj(), b7) / b8
        return b9
    def fonk5(self, signal):
        '''Return class1 modes using singular value decomposition.'''
        b9 = self.fonk4(signal)
        u, s, b10 = np.linalg.svd(b9, full_matrices=True)
        self.b4 = u[:, :self.b2]
        self.b5 = s[:self.b2]
    def fonk6(self):
        '''Compute the principal components of each mode.'''
        b11 = self.fonk3(self.b1)
        b12 = np.dot(self.b4.T, b11.T)
        return b12
    def fonk7(self):
        '''Plot the frequency transform of the time coefficients of the modes.'''
        b12 = self.fonk6()
        a1 = 700
        b13 = 2 ** 13
        b14 = []
        for i in range(self.b2):
            freq, b15 = welch(b12[i, :], nperseg=b13, b13=b13, noverlap=b13
                               b16 = a1)
            b14.append(b15)
        b14 = np.array(b14)
        fig, b17 = plt.subplots()
        for i in range(self.b2):
            b17.plot(freq, b14[i, :], b18 = b29'Mode {i + 1}')
        b17.set_xlim(0, 10)
        b17.set_xlabel('Frequency (Hz)')
        b17.set_ylabel('Spectral Density (1/Hz)')
        b17.legend(b19 = 'best')
        plt.show()
    def fonk8(self):
        '''Execute class1 and return class1 modes and their corresponding eigenvalues.'''
        self.fonk5(self.b1)
        return self.b4, self.b5
    def fonk9(self):
        '''Visualize class1 modes.'''
        self.fonk2(Plot_press)
        for i in range(self.b2):
            self.b3['id'](self.b4[:, i], ['red', 'white', 'blue'], b20 = True, num=i + 1)
        self.fonk7()
class class2(class1):
    def fonk10(self, b1, b2, b21, b22, b23):
        super().fonk10(b1, b2)
        self.b21 = b21
        self.b22 = b22
        self.b23 = b23
        self.b24 = []
        self.b25 = []
    def fonk11(self, signal):
        '''Remove frequencies that lie outside the range of the bandpass.'''
        b26 = self.fonk3(signal)
        b27 = len(b26)
        b28 = self.b23 / b27
        b29 = np.linspace(start=-self.b23 / 2, stop=self.b23 / 2 - b28, num=self.b1.shape[0]).T
        b30 = ((self.b21 < abs(b29)) & (abs(b29) < self.b22)).reshape(-1, 1)
        b31 = np.fft.fft(b26, axis=0)
        b32 = np.fft.fftshift(b31) / b27
        b33 = np.fft.ifftshift(np.multiply(b30.astype(np.int), b32), axis=0)
        b34 = np.fft.ifft(b33, axis=0)
        return np.real(b34)
    def fonk12(self, signal):
        '''Create an analytic signal using the Hilbert transform.'''
        b33 = self.fonk11(signal)
        b35 = hilbert(b33, axis=0)
        return b35
    def fonk13(self, signal):
        '''Return class2 modes.'''
        b35 = self.fonk12(signal)
        b9 = self.fonk4(b35)
        u, s, b10 = np.linalg.svd(np.array(b9))
        self.b24 = u[:, :self.b2]
        self.b25 = s[:self.b2]
    def fonk14(self):
        '''Execute class1 and return class1 modes and their corresponding eigenvalues.'''
        self.fonk13(self.b1)
        return self.b24, self.b25
    def fonk15(self, mode_no):
        '''Visualize the animated movie of class1 mode.'''
        b36 = self.b24[:, mode_no]
        b37 = b36.reshape(-1, 1)
        b38 = np.exp(1j * np.linspace(0, 2 * np.pi, 100)).reshape(1, -1)
        b39 = np.real(b37 * b38)
        self.fonk2(Plot_press)
        plt.ion()
        for i in range(100):
            b40 = b39[:, i]
            self.b3['id'](b40, ['red', 'white', 'blue'], b20 = False, num=1)
            plt.pause(0.1)
            plt.clf()
if b41 = = "__main__":
    b42 = np.random.rand(100, 10)
    b43 = class1(b42, 3)
    b43.fonk8()
    b43.fonk9()