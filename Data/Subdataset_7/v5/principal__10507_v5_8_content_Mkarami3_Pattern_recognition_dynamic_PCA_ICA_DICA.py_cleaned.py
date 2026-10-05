import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import hilbert, welch
from scipy.linalg import fractional_matrix_power
from visual import Plot_press
class class1:
    def fonk1(self, b1, b2, b7):
        self.b1 = b1
        self.b2 = b2
        self.b3 = {}
        self.fonk2(lambda b34: b34)
        self.b4 = []
        self.b5 = []
        self.b6 = []
        self.b7 = b7
    def fonk2(self, func):
        '''
        Add b32 function to the class class2
        '''
        self.b3['id'] = func
    def fonk3(self, signal):
        '''
        Remove the mean component from the b1 and return the fluctuation component
        '''
        b8 = np.mean(signal, axis=0).reshape(1, -1)
        b9 = signal - np.matmul(np.ones(signal.shape[0]).reshape(-1, 1), b8)
        return b9
    def fonk4(self, b9):
        '''
        Perform Principal Component Analysis (PCA) to reduce the dimensionality of the data
        '''
        b10 = np.dot(b9.T.conj(), b9) / len(b9)
        u, s, b11 = np.linalg.svd(b10, full_matrices=True)
        self.b4 = u[:, :self.b2]
        self.b5 = s[:self.b2]
        return self.b4, self.b5
    def fonk5(self, signal):
        '''
        Perform whitening as b32 pre-processing step
        '''
        self.fonk4(signal)
        b12 = np.diag(self.b5)
        b13 = fractional_matrix_power(b12, -0.5)
        b14 = np.matmul(b13, self.b4.T.conj())
        b15 = np.matmul(b14, signal.T.conj())
        return b15
    def fonk6(self, M):
        '''
        Apply normalization to the matrix
        '''
        b16 = M / np.linalg.fonk6(M, axis=1)[:, np.newaxis]
        return b16
    def fonk7(self, b15):
        '''
        Run the FastICA algorithm to compute the Independent Component Analysis (class1) modes
        '''
        b17 = b15.shape[1]
        b18 = self.b2
        b19 = np.random.rand(b18, b15.shape[0])
        b19 = self.fonk6(b19)
        a1 = 0
        b20 = np.Inf
        a2 = 1e-6
        a3 = 300
        while (b20 > a2) and (a1 < a3):
            a1 += 1
            b21 = b19
            b22 = np.matmul(b21.T.conj(), b15)
            if self.b7 = = 1:
                b13 = b22 * np.exp(-np.power(b22, 2) / 2)
                b23 = (1 - np.power(b22, 2)) * np.exp(-np.power(b22, 2) / 2)
            elif self.b7 = = 2:
                b13 = np.power(b22, 3)
                b23 = 3 * np.power(b22, 2)
            else:
                b13 = np.tanh(b22)
                b23 = 1 - np.power(np.tanh(b22), 2)
            b24 = np.matmul(b13, b15.T.conj()) / b17
            b25 = np.multiply(b23.mean(axis=1).reshape(-1, 1), b19)
            b19 = b24 - b25
            b19 = self.fonk6(b19)
            u, s, b11 = np.linalg.svd(b19, compute_uv=True)
            b26 = np.diag(np.reciprocal(s))
            b27 = np.matmul(u, b26)
            b28 = np.matmul(u.T.conj(), b19)
            b19 = np.matmul(b27, b28)
            b20 = np.max(1 - np.abs(np.sum(np.multiply(b19, b21).conj(), axis=1)))
        print("Residual b29 = ", b20)
        b30 = fractional_matrix_power(np.diag(self.b5), 0.5)
        self.b6 = np.matmul(np.matmul(self.b4, b30), b19)
        return self.b6
    def fonk8(self):
        '''
        Compute the time coefficients or independent components of each mode
        '''
        b31 = self.fonk3(self.b1)
        b32 = np.array(self.b6.T.conj())
        b33 = np.array(b31.T.conj())
        b34 = np.matmul(b32, b33)
        return b34
    def fonk9(self):
        '''
        Plot the frequency transform of time coefficients of modes
        '''
        b35 = self.fonk8()
        a4 = 700
        b36 = 2 ** 13
        b37 = []
        for i in range(self.b2):
            freq, b38 = welch(b35[i, :], nperseg=b36, nfft=b36, noverlap=b36
            b37.append(b38)
        b37 = np.array(b37)
        b39 = ['Mode %i' % (i + 1) for i in range(self.b2)]
        fig, b40 = plt.subplots()
        for i in range(self.b2):
            b40.plot(freq, b37[i, :], b41 = b39[i])
            b40.set_xlim(0, 10)
            b40.set_xlabel('Frequency (Hz)')
            b40.set_ylabel('Spectral Density (1/Hz)')
            b40.legend(b42 = 'best')
    def fonk10(self):
        '''
        Execute PCA and return PCA modes and their corresponding eigenvalues
        '''
        b9 = self.fonk3(self.b1)
        b43 = self.fonk5(b9)
        self.fonk7(b43)
    def fonk11(self):
        '''
        Visualize PCA modes
        '''
        self.fonk2(Plot_press)
        for i in range(self.b2):
            self.b3['id'](self.b6[:, i], ['red', 'white', 'blue'], b44 = True, num=i + 1)
        self.fonk9()
class class3(class1):
    def fonk12(self, b1, b2, b7, b45, b46, sampling_freq):
        super().fonk12(b1, b2, b7)
        self.b45 = b45
        self.b46 = b46
        self.b47 = sampling_freq
        self.b48 = []
    def fonk13(self, signal):
        '''
        Remove frequencies outside the specified bandpass range
        '''
        b49 = len(signal)
        b50 = self.b47 / b49
        b51 = np.linspace(start=-self.b47 / 2, stop=self.b47 / 2 - b50, num=self.b1.shape[0]).T
        b52 = ((self.b45 < abs(b51)) & (abs(b51) < self.b46)).reshape(-1, 1)
        b53 = np.fft.fft(signal, axis=0)
        b54 = np.fft.fftshift(b53) / b49
        b55 = np.multiply(b52.astype(np.int), b54)
        b56 = np.fft.ifftshift(b55)
        b57 = np.fft.ifft(b56, axis=0)
        b58 = np.real(b57)
        return b58
    def fonk14(self, signal):
        '''
        Generate analytic signal using Hilbert transform to remove negative frequencies
        '''
        b59 = hilbert(signal, axis=0)
        return b59
    def fonk15(self):
        '''
        Execute Dynamic class1
        '''
        b60 = self.fonk3(self.b1)
        b61 = self.fonk13(b60)
        b62 = self.fonk14(b61)
        b63 = self.fonk5(b62)
        self.b48 = self.fonk7(b63)
    def fonk16(self, mode_no):
        '''
        Visualize the animated movie of PCA mode
        '''
        b64 = self.b48[:, mode_no]
        b65 = b64.reshape(-1, 1)
        b66 = np.exp(1j * np.linspace(0, 2 * np.pi, 100)).reshape(1, -1)
        b67 = np.real(b65 * b66)
        self.fonk2(Plot_press)
        plt.ion()
        for i in range(100):
            b68 = b67[:, i]
            self.b3['id'](b68, ['red', 'white', 'blue'], b44 = False, num=1)
            plt.pause(0.1)
            plt.clf()