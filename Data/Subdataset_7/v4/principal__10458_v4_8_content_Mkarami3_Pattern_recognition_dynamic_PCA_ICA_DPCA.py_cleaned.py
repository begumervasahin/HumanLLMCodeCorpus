import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import hilbert, welch
from visual import Plot_press
class class1:
    def fonk1(self, b1, b2):
        self.b1 = b1
        self.b2 = b2
        self.b3 = {}
        self.fonk2(lambda b15: b15)
        self.b4 = []
        self.b5 = []
    def fonk2(self, func):
        '''
        Add b13 function to the class.
        '''
        b6 = 'id'
        self.b3[b6] = func
    def fonk3(self, signal):
        '''
        Remove the mean component from the b1
        and return the fluctuation component.
        '''
        b7 = np.mean(signal, axis=0).reshape(1, -1)
        b8 = signal - np.matmul(np.ones(signal.shape[0]).reshape(-1, 1), b7)
        return b8
    def fonk4(self, signal):
        '''
        Return the covariance of the preprocessed b1.
        '''
        b8 = self.fonk3(signal)
        b9 = len(b8)
        b10 = np.dot(b8.T.conj(), b8) / b9
        return b10
    def fonk5(self, signal):
        '''
        Return class1 modes using singular value decomposition.
        '''
        b10 = self.fonk4(signal)
        u, s, b11 = np.linalg.fonk5(b10, full_matrices=True)
        self.b4 = u[:, 0:self.b2]
        self.b5 = s[0:self.b2]
    def fonk6(self):
        '''
        Compute the time_coefficient, or principal components,
        of each mode.
        '''
        b12 = self.fonk3(self.b1)
        b13 = np.array(self.b4.T)
        b14 = np.array(b12.T)
        b15 = np.matmul(b13, b14)
        return b15
    def fonk7(self):
        '''
        Plot the frequency transform of the time coefficient of Modes.
        '''
        b16 = self.fonk6()
        a1 = 700
        b17 = 2 ** 13
        b18 = []
        for i in range(5):
            freq, b19 = welch(b16[i, :], nperseg=b17, nfft=b17, noverlap=b17 / 2,
                               b20 = a1)
            b18.append(b19)
        b18 = np.array(b18)
        b21 = [b33'Mode {i + 1}' for i in range(5)]
        fig, b22 = plt.subplots()
        for i in range(5):
            b22.plot(freq, b18[i, :], b23 = b21[i])
            b22.set_xlim(0, 10)
            b22.set_xlabel('Frequency (Hz)')
            b22.set_ylabel('Spectral Density (1/Hz)')
            b22.legend(b24 = 'best')
        plt.show()
    def fonk8(self):
        '''
        Execute class1 and return class1 modes and their corresponding
        eigenvalues.
        '''
        self.fonk5(self.b1)
        return self.b4, self.b5
    def fonk9(self):
        '''
        Visualize class1 modes.
        '''
        self.fonk2(Plot_press)
        for i in range(self.b2):
            self.b3['id'](self.b4[:, i], ['red', 'white', 'blue'], b25 = True, num=i + 1)
        self.fonk7()
class class2(class1):
    def fonk10(self, b1, b2, b26, b27, sampling_freq):
        super().fonk10(b1, b2)
        self.b26 = b26
        self.b27 = b27
        self.b20 = sampling_freq
        self.b28 = []
        self.b29 = []
    def fonk11(self, signal):
        '''
        Remove frequencies that lie outside the range of bandpass.
        '''
        b30 = self.fonk3(signal)
        b31 = len(b30)
        b32 = self.b20 / b31
        b33 = np.linspace(start=-self.b20 / 2, stop=self.b20 / 2 - b32, num=self.b1.shape[0]).T
        b34 = ((self.b26 < abs(b33)) & (abs(b33) < self.b27)).reshape(-1, 1)
        b35 = np.fft.fft(b30, axis=0)
        b36 = np.fft.fftshift(b35) / b31
        b37 = np.multiply(b34.astype(np.int), b36)
        b38 = np.fft.ifftshift(b37)
        b39 = np.fft.ifft(b38, axis=0)
        b40 = np.real(b39)
        return b40
    def fonk12(self, signal):
        '''
        Create an analytic signal using the Hilbert transform.
        This will remove negative frequencies in the filtered signals.
        '''
        b41 = self.fonk11(signal)
        b42 = hilbert(b41, axis=0)
        return b42
    def fonk13(self, signal):
        '''
        Return class2 modes.
        '''
        b42 = self.fonk12(signal)
        b10 = self.fonk4(b42)
        u, s, b11 = np.linalg.fonk5(np.array(b10))
        self.b28 = u[:, 0:self.b2]
        self.b29 = s[0:self.b2]
    def fonk14(self):
        '''
        Execute class1 and return class1 modes and their corresponding eigenvalues.
        '''
        self.fonk13(self.b1)
        return self.b28, self.b29
    def fonk15(self, mode_no):
        '''
        Visualize the animated movie of class1 mode.
        '''
        b43 = self.b28[:, mode_no]
        b44 = b43.reshape(-1, 1)
        b45 = np.exp(1j * np.linspace(0, 2 * np.pi, 100)).reshape(1, -1)
        b46 = np.real(b44 * b45)
        self.fonk2(Plot_press)
        plt.ion()
        for i in range(100):
            b47 = b46[:, i]
            self.b3['id'](b47, ['red', 'white', 'blue'], b25 = False, num=1)
            plt.pause(0.1)
            plt.clf()
if b48 = = "__main__":
    b49 = np.random.rand(100, 10)
    b50 = class1(b49, 3)
    b50.fonk14()
    b50.fonk15()