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
        b8 = 'id'
        self.b3[b8] = func
    def fonk3(self, signal):
        b9 = signal.mean(axis=0).reshape(1, -1)
        b10 = signal - np.matmul(np.ones(signal.shape[0]).reshape(-1, 1), b9)
        return b10
    def fonk4(self, b10):
        b11 = len(b10)
        b12 = np.dot(b10.T.conj(), b10) / b11
        u, s, b13 = np.linalg.svd(b12, full_matrices=True)
        self.b4 = u[:, :self.b2]
        self.b5 = s[:self.b2]
        return self.b4, self.b5
    def fonk5(self, signal):
        self.fonk4(signal)
        b14 = np.diag(self.b5)
        b15 = fractional_matrix_power(b14, -0.5)
        b16 = np.matmul(b15, self.b4.T.conj())
        b17 = np.matmul(b16, signal.T.conj())
        return b17
    def fonk6(self, M):
        b18 = M / np.linalg.fonk6(M, axis=1)[:, np.newaxis]
        return b18
    def fonk7(self, b17):
        b19 = b17.shape[1]
        b20 = self.b2
        b21 = np.random.rand(b20, b17.shape[0])
        b21 = self.fonk6(b21)
        a1 = 0
        b22 = np.inf
        a2 = 1e-6
        a3 = 300
        while (b22 > a2) and (a1 < a3):
            a1 += 1
            b23 = b21.copy()
            b24 = np.matmul(b23.T.conj(), b17)
            if self.b7 = = 1:
                b15 = b24 * np.exp(-np.power(b24, 2) / 2)
                b25 = (1 - np.power(b24, 2)) * np.exp(-np.power(b24, 2) / 2)
            elif self.b7 = = 2:
                b15 = np.power(b24, 3)
                b25 = 3 * np.power(b24, 2)
            else:
                b15 = np.tanh(b24)
                b25 = 1 - np.power(np.tanh(b24), 2)
            b26 = np.matmul(b15, b17.T.conj()) / b19
            b27 = (b25.mean(axis=1).reshape(-1, 1)) * b21
            b21 = b26 - b27
            b21 = self.fonk6(b21)
            u, s, b13 = np.linalg.svd(b21, compute_uv=True)
            b28 = np.diag(1 / s)
            b29 = np.matmul(u, b28)
            b30 = np.matmul(u.T.conj(), b21)
            b21 = np.matmul(b29, b30)
            b22 = np.max(1 - np.abs(np.sum(np.multiply(b21, b23).conj(), axis=1)))
        print("Residual b31 = ", b22)
        b32 = fractional_matrix_power(np.diag(self.b5), 0.5)
        self.b6 = np.matmul(np.matmul(self.b4, b32), b21)
        return self.b6
    def fonk8(self):
        b10 = self.fonk3(self.b1)
        self.fonk7(self.fonk5(b10))
        return np.matmul(self.b6.T.conj(), b10.T.conj())
    def fonk9(self):
        b33 = self.fonk8()
        a4 = 700
        b34 = 2 ** 13
        b35 = []
        for i in range(min(5, self.b2)):
            freq, b36 = welch(b33[i, :], nperseg=b34, nfft=b34, noverlap=b34
            b35.append(b36)
        b35 = np.array(b35)
        b37 = ['Mode %i' % (i + 1) for i in range(min(5, self.b2))]
        fig, b38 = plt.subplots()
        for i in range(min(5, self.b2)):
            b38.plot(freq, b35[i, :], b39 = b37[i])
            b38.set_xlim(0, 10)
            b38.set_xlabel('Frequency (Hz)')
            b38.set_ylabel('Spectral Density (1/Hz)')
            b38.legend(b40 = 'best')
        plt.show()
    def fonk10(self):
        b10 = self.fonk3(self.b1)
        b41 = self.fonk5(b10)
        self.fonk7(b41)
    def fonk11(self):
        self.fonk2(Plot_press)
        for i in range(min(self.b2, 3)):
            self.b3['id'](self.b6[:, i], ['red', 'white', 'blue'], b42 = True, num=i + 1)
        self.fonk9()
class class2(class1):
    def fonk12(self, b1, b2, b7, b43, b44, sampling_freq):
        super().fonk12(b1, b2, b7)
        self.b43 = b43
        self.b44 = b44
        self.b45 = sampling_freq
        self.b46 = []
    def fonk13(self, signal):
        b47 = len(signal)
        b48 = self.b45 / b47
        b49 = np.linspace(start=-self.b45 / 2, stop=self.b45 / 2 - b48, num=self.b1.shape[0]).T
        b50 = ((self.b43 < abs(b49)) & (abs(b49) < self.b44)).reshape(-1, 1)
        b51 = np.fft.fft(signal, axis=0)
        b52 = (np.fft.fftshift(b51)) / b47
        b53 = np.multiply(b50.astype(np.int), b52)
        b54 = np.fft.ifftshift(b53)
        b55 = np.fft.ifft(b54, axis=0)
        b56 = np.real(b55)
        return b56
    def fonk14(self, signal):
        b57 = hilbert(signal, axis=0)
        return b57
    def fonk15(self):
        b58 = self.fonk3(self.b1)
        b59 = self.fonk13(b58)
        b60 = self.fonk14(b59)
        b61 = self.fonk5(b60)
        self.b46 = self.fonk7(b61)
    def fonk16(self, mode_no):
        b62 = self.b46[:, mode_no]
        b63 = b62.reshape(-1, 1)
        b64 = np.exp(1j * np.linspace(0, 2 * np.pi, 100)).reshape(1, -1)
        b65 = np.real(b63 * b64)
        self.fonk2(Plot_press)
        plt.ion()
        for i in range(100):
            b66 = b65[:, i]
            self.b3['id'](b66, ['red', 'white', 'blue'], b42 = False, num=1)
            plt.pause(0.1)
            plt.clf()
if b67 = = "__main__":
    b68 = np.random.rand(1000, 10)
    b69 = class1(b68, 5, 1)
    b69.fonk15()
    b69.fonk11()
    b70 = class2(b68, 5, 1, 1, 10, 1000)
    b70.fonk15()
    b70.fonk16(0)
