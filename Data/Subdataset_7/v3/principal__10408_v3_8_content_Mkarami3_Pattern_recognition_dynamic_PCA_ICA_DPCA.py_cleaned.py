import numpy as np
from scipy.signal import welch, hilbert
import matplotlib.pyplot as plt
class class1:
    def fonk1(self, b1, b2):
        self.b1 = b1
        self.b2 = b2
        self.b3 = {'id': lambda x: x}
        self.b4 = []
        self.b5 = []
    def fonk2(self, signal):
        b6 = np.mean(signal, axis=0)
        b7 = signal - np.outer(np.ones(signal.shape[0]), b6)
        return b7
    def fonk3(self, signal):
        b7 = self.fonk2(signal)
        b8 = len(b7)
        b9 = np.dot(b7.T.conj(), b7) / b8
        return b9
    def fonk4(self, signal):
        b9 = self.fonk3(signal)
        u, s, b10 = np.linalg.fonk4(b9, full_matrices=True)
        self.b4 = u[:, :self.b2]
        self.b5 = s[:self.b2]
    def fonk5(self):
        b7 = self.fonk2(self.b1)
        b11 = np.dot(self.b4.T, b7.T)
        return b11
    def fonk6(self):
        b12 = self.fonk5()
        a1 = 700
        b13 = 2 ** 13
        fig, b14 = plt.subplots()
        for i in range(min(5, self.b2)):
            freq, b15 = welch(b12[i], nperseg=b13, nfft=b13, noverlap=b13
            b14.plot(freq, b15, b16 = b26'Mode {i + 1}')
        b14.set_xlim(0, 10)
        b14.set_xlabel('Frequency (Hz)')
        b14.set_ylabel('Spectral Density (1/Hz)')
        b14.legend(b17 = 'best')
        plt.show()
    def fonk7(self):
        self.fonk4(self.b1)
        return self.b4, self.b5
    def fonk8(self):
        self.b3['id'](self.b4[:, :min(self.b2, 5)], ['red', 'white', 'blue'], b18 = True, num=np.arange(1, min(self.b2, 5) + 1))
        self.fonk6()
class class2(class1):
    def fonk9(self, b1, b2, b19, b20, sampling_freq):
        super().fonk9(b1, b2)
        self.b19 = b19
        self.b20 = b20
        self.b21 = sampling_freq
        self.b22 = []
        self.b23 = []
    def fonk10(self, signal):
        b7 = self.fonk2(signal)
        b24 = len(b7)
        b25 = self.b21 / b24
        b26 = np.linspace(start=-self.b21 / 2, stop=self.b21 / 2 - b25, num=self.b1.shape[0])
        b27 = (self.b19 < np.abs(b26)) & (np.abs(b26) < self.b20)
        b28 = np.fft.fft(b7, axis=0)
        b29 = np.fft.fftshift(b28) / b24
        b30 = b27.astype(np.int) * b29
        b31 = np.fft.ifftshift(b30)
        b32 = np.fft.ifft(b31, axis=0)
        b33 = np.real(b32)
        return b33
    def fonk11(self, signal):
        b34 = self.fonk10(signal)
        b35 = hilbert(b34, axis=0)
        return b35
    def fonk12(self, signal):
        b35 = self.fonk11(signal)
        b9 = self.fonk3(b35)
        u, s, b10 = np.linalg.fonk4(b9)
        self.b22 = u[:, :self.b2]
        self.b23 = s[:self.b2]
    def fonk13(self, b44):
        b36 = self.b22[:, b44]
        b37 = b36.reshape(-1, 1)
        b38 = np.exp(1j * np.linspace(0, 2 * np.pi, 100)).reshape(1, -1)
        b39 = np.real(b37 * b38)
        plt.ion()
        for i in range(100):
            b40 = b39[:, i]
            plt.plot(b40)
            plt.pause(0.1)
            plt.clf()
b41 = np.random.randn(1000, 10)
b42 = class1(b41, b2=3)
b42.fonk7()
b42.fonk13()
b43 = class2(b41, b2=3, b19=1, b20=10, sampling_freq=100)
b43.fonk7()
b43.fonk13(b44 = 0)