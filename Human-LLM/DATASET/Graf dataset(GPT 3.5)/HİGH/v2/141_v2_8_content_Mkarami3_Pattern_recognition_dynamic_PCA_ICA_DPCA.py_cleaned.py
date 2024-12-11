import numpy as np
from scipy.signal import hilbert, welch
import matplotlib.pyplot as plt
class class1:
    def fonk1(self, b1, b2):
        self.b1 = b1
        self.b2 = b2
        self.b3 = {}
        self.fonk2(lambda b15: b15)
        self.b4 = []
        self.b5 = []
    def fonk2(self, func):
        b6 = 'id'
        self.b3[b6] = func
    def fonk3(self, signal):
        b7 = signal.mean(axis=0).reshape(1, -1)
        b8 = signal - np.matmul(np.ones(signal.shape[0]).reshape(-1, 1), b7)
        return b8
    def fonk4(self, signal):
        b8 = self.fonk3(signal)
        b9 = len(b8)
        b10 = np.dot(b8.T.conj(), b8) / b9
        return b10
    def fonk5(self, signal):
        b10 = self.fonk4(signal)
        u, s, b11 = np.linalg.fonk5(b10, full_matrices=True)
        self.b4 = u[:, :self.b2]
        self.b5 = s[:self.b2]
    def fonk6(self):
        b12 = self.fonk3(self.b1)
        b13 = np.array(self.b4.T)
        b14 = np.array(b12.T)
        b15 = np.matmul(b13, b14)
        return b15
    def fonk7(self):
        b16 = self.fonk6()
        a1 = 700
        b17 = 2 ** 13
        b18 = []
        for i in range(min(5, self.b2)):
            freq, b19 = welch(b16[i, :], nperseg=b17, nfft=b17, noverlap=b17
            b18.append(b19)
        b18 = np.array(b18)
        b20 = [b33'Mode {i + 1}' for i in range(min(5, self.b2))]
        fig, b21 = plt.subplots()
        for i in range(min(5, self.b2)):
            b21.plot(freq, b18[i, :], b22 = b20[i])
        b21.set_xlim(0, 10)
        b21.set_xlabel('Frequency (Hz)')
        b21.set_ylabel('Spectral Density (1/Hz)')
        b21.legend(b23 = 'best')
        plt.show()
    def fonk8(self):
        self.fonk5(self.b1)
        return self.b4, self.b5
    def fonk9(self):
        self.fonk2(Plot_press)
        for i in range(min(self.b2, 5)):
            self.b3['id'](self.b4[:, i], ['red', 'white', 'blue'], b24 = True, num=i + 1)
        self.fonk7()
class class2(class1):
    def fonk10(self, b1, b2, b25, b26, sampling_freq):
        super().fonk10(b1, b2)
        self.b25 = b25
        self.b26 = b26
        self.b27 = sampling_freq
        self.b28 = []
        self.b29 = []
    def fonk11(self, signal):
        b30 = self.fonk3(signal)
        b31 = len(b30)
        b32 = self.b27 / b31
        b33 = np.linspace(start=-self.b27 / 2, stop=self.b27 / 2 - b32, num=self.b1.shape[0]).T
        b34 = ((self.b25 < np.abs(b33)) & (np.abs(b33) < self.b26)).reshape(-1, 1)
        b35 = np.fft.fft(b30, axis=0)
        b36 = np.fft.fftshift(b35) / b31
        b37 = np.multiply(b34.astype(np.int), b36)
        b38 = np.fft.ifftshift(b37)
        b39 = np.fft.ifft(b38, axis=0)
        b40 = np.real(b39)
        return b40
    def fonk12(self, signal):
        b41 = self.fonk11(signal)
        b42 = hilbert(b41, axis=0)
        return b42
    def fonk13(self, signal):
        b42 = self.fonk12(signal)
        b10 = self.fonk4(b42)
        u, s, b11 = np.linalg.fonk5(np.array(b10))
        self.b28 = u[:, :self.b2]
        self.b29 = s[:self.b2]
    def fonk14(self):
        self.fonk13(self.b1)
        return self.b28, self.b29
    def fonk15(self, b51):
        b43 = self.b28[:, b51]
        b44 = b43.reshape(-1, 1)
        b45 = np.exp(1j * np.linspace(0, 2 * np.pi, 100)).reshape(1, -1)
        b46 = np.real(b44 * b45)
        plt.ion()
        for i in range(100):
            b47 = b46[:, i]
            plt.plot(b47)
            plt.pause(0.1)
            plt.clf()
b48 = np.random.randn(1000, 10)
b49 = class1(b48, b2=3)
b49.fonk14()
b49.fonk15()
b50 = class2(b48, b2=3, b25=1, b26=10, sampling_freq=100)
b50.fonk14()
b50.fonk15(b51 = 0)