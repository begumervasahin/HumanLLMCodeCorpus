import numpy as np
from scipy.signal import hilbert, welch
import matplotlib.pyplot as plt
from scipy.linalg import fractional_matrix_power
class class1:
    def fonk1(self, b1, b2, b7):
        self.b1 = b1
        self.b2 = b2
        self.b3 = {}
        self.fonk2(lambda x: x)
        self.b4 = []
        self.b5 = []
        self.b6 = []
        self.b7 = b7
    def fonk2(self, func):
        self.b3['id'] = func
    def fonk3(self, signal):
        b8 = np.mean(signal, axis=0)
        b9 = signal - np.outer(np.ones(signal.shape[0]), b8)
        return b9
    def fonk4(self, b9):
        b10 = np.dot(b9.T.conj(), b9) / len(b9)
        u, s, b11 = np.linalg.svd(b10, full_matrices=True)
        self.b4 = u[:, :self.b2]
        self.b5 = s[:self.b2]
        return self.b4, self.b5
    def fonk5(self, signal):
        self.fonk4(signal)
        b12 = np.diag(self.b5)
        b13 = fractional_matrix_power(b12, -0.5)
        b14 = np.dot(b13, self.b4.T.conj())
        b15 = np.dot(b14, signal.T.conj())
        return b15
    def fonk6(self, M):
        b16 = M / np.linalg.fonk6(M, axis=1)[:, np.newaxis]
        return b16
    def fonk7(self, b15):
        b17 = b15.shape[1]
        b18 = self.b2
        b19 = np.random.rand(b18, b15.shape[0])
        b19 = self.fonk6(b19)
        a1 = 0
        b20 = np.inf
        a2 = 1e-6
        a3 = 300
        while (b20 > a2) and (a1 < a3):
            a1 += 1
            b21 = b19.copy()
            b22 = np.dot(b21.T.conj(), b15)
            if self.b7 = = 1:
                b13 = b22 * np.exp(-np.power(b22, 2) / 2)
                b23 = (1 - np.power(b22, 2)) * np.exp(-np.power(b22, 2) / 2)
            elif self.b7 = = 2:
                b13 = np.power(b22, 3)
                b23 = 3 * np.power(b22, 2)
            else:
                b13 = np.tanh(b22)
                b23 = 1 - np.power(np.tanh(b22), 2)
            b24 = np.dot(b13, b15.T.conj()) / b17
            b25 = (b23.mean(axis=1).reshape(-1, 1)) * b19
            b19 = b24 - b25
            b19 = self.fonk6(b19)
            u, s, b11 = np.linalg.svd(b19, compute_uv=True)
            b26 = np.diag(1 / s)
            b27 = np.dot(u, b26)
            b28 = np.dot(u.T.conj(), b19)
            b19 = np.dot(b27, b28)
            b20 = np.max(1 - np.abs(np.sum(np.multiply(b19, b21).conj(), axis=1)))
        print("Residual b29 = ", b20)
        b30 = fractional_matrix_power(np.diag(self.b5), 0.5)
        self.b6 = np.dot(np.dot(self.b4, b30), b19)
        return self.b6
    def fonk8(self):
        b9 = self.fonk3(self.b1)
        self.fonk7(self.fonk5(b9))
        return np.dot(self.b6.T.conj(), b9.T.conj())
    def fonk9(self):
        b31 = self.fonk8()
        a4 = 700
        b32 = 2 ** 13
        b33 = []
        for i in range(min(5, self.b2)):
            freq, b34 = welch(b31[i, :], nperseg=b32, nfft=b32, noverlap=b32
            b33.append(b34)
        b33 = np.array(b33)
        b35 = ['Mode %i' % (i + 1) for i in range(min(5, self.b2))]
        fig, b36 = plt.subplots()
        for i in range(min(5, self.b2)):
            b36.plot(freq, b33[i, :], b37 = b35[i])
            b36.set_xlim(0, 10)
            b36.set_xlabel('Frequency (Hz)')
            b36.set_ylabel('Spectral Density (1/Hz)')
            b36.legend(b38 = 'best')
        plt.show()
    def fonk10(self):
        b9 = self.fonk3(self.b1)
        b39 = self.fonk5(b9)
        self.fonk7(b39)
    def fonk11(self):
        self.fonk2(Plot_press)
        for i in range(min(self.b2, 3)):
            self.b3['id'](self.b6[:, i], ['red', 'white', 'blue'], b40 = True, num=i + 1)
        self.fonk9()
class class2(class1):
    def fonk12(self, b1, b2, b7, b41, b42, sampling_freq):
        super().fonk12(b1, b2, b7)
        self.b41 = b41
        self.b42 = b42
        self.b43 = sampling_freq
        self.b44 = []
    def fonk13(self, signal):
        b45 = len(signal)
        b46 = self.b43 / b45
        b47 = np.linspace(start=-self.b43 / 2, stop=self.b43 / 2 - b46, num=self.b1.shape[0]).T
        b48 = ((self.b41 < abs(b47)) & (abs(b47) < self.b42)).reshape(-1, 1)
        b49 = np.fft.fft(signal, axis=0)
        b50 = (np.fft.fftshift(b49)) / b45
        b51 = np.multiply(b48.astype(np.int), b50)
        b52 = np.fft.ifftshift(b51)
        b53 = np.fft.ifft(b52, axis=0)
        b54 = np.real(b53)
        return b54
    def fonk14(self, signal):
        b55 = hilbert(signal, axis=0)
        return b55
    def fonk15(self):
        b56 = self.fonk3(self.b1)
        b57 = self.fonk13(b56)
        b58 = self.fonk14(b57)
        b59 = self.fonk5(b58)
        self.b44 = self.fonk7(b59)
    def fonk16(self, mode_no):
        b60 = self.b44[:, mode_no]
        b61 = b60.reshape(-1, 1)
        b62 = np.exp(1j * np.linspace(0, 2 * np.pi, 100)).reshape(1, -1)
        b63 = np.real(b61 * b62)
        self.fonk2(Plot_press)
        plt.ion()
        for i in range(100):
            b64 = b63[:, i]
            self.b3['id'](b64, ['red', 'white', 'blue'], b40 = False, num=1)
            plt.pause(0.1)
            plt.clf()
if b65 = = "__main__":
    b66 = np.random.rand(1000, 10)
    b67 = class1(b66, 5, 1)
    b67.fonk15()
    b67.fonk11()
    b68 = class2(b66, 5, 1, 1, 10, 1000)
    b68.fonk15()
    b68.fonk16(0)
