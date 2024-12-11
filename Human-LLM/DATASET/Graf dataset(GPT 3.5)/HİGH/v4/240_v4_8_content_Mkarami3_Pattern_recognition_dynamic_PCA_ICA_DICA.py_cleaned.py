import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import hilbert, welch
from scipy.linalg import fractional_matrix_power
from visual import Plot_press
class class1(object):
    def fonk1(self, b1, b2, b7):
        self.b1 = b1
        self.b2 = b2
        self.b3 = {}
        self.fonk2(lambda b39: b39)
        self.b4 = []
        self.b5 = []
        self.b6 = []
        self.b7 = b7
    def fonk2(self, func):
        '''
        Add b37 function to the class class2
        '''
        b8 = 'id'
        self.b3[b8] = func
    def fonk3(self, signal):
        '''
        Remove the mean component from the b1 and return the fluctuation component
        '''
        b9 = signal.mean(axis=0).reshape(1, -1)
        b10 = signal - np.matmul(np.ones(signal.shape[0]).reshape(-1, 1), b9)
        return b10
    def fonk4(self, b10):
        '''
        Perform Principal Component Analysis (PCA) to reduce the dimensionality of the data
        '''
        b11 = len(b10)
        b12 = np.dot(b10.T.conj(), b10) / b11
        u, s, b13 = np.linalg.svd(b12, full_matrices=True)
        self.b4 = u[:, 0:self.b2]
        self.b5 = s[0:self.b2]
        return self.b4, self.b5
    def fonk5(self, signal):
        '''
        Perform whitening as b37 pre-processing step
        '''
        self.fonk4(signal)
        b14 = np.diag(self.b5)
        b15 = fractional_matrix_power(b14, -0.5)
        b16 = np.matmul(b15, self.b4.T.conj())
        b17 = np.matmul(b16, signal.T.conj())
        return b17
    def fonk6(self, M):
        '''
        Apply normalization to the matrix
        '''
        b18 = np.power(M, 2)
        b19 = np.sum(b18, axis=1)
        b20 = np.power(b19, 0.5)
        b21 = (M.T / b20).T
        return b21
    def fonk7(self, b17):
        '''
        Run the FastICA algorithm to compute the Independent Component Analysis (class1) modes
        '''
        b22 = b17.shape[1]
        b23 = self.b2
        b24 = np.random.rand(b23, b17.shape[0])
        b24 = self.fonk6(b24)
        a1 = 0
        b25 = np.Inf
        a2 = 1e-6
        a3 = 300
        while (b25 > a2) and (a1 < a3):
            a1 += 1
            b26 = b24
            b27 = np.matmul(b26.T.conj(), b17)
            if self.b7 = = 1:
                b15 = np.multiply(b27, np.exp(-np.power(b27, 2) / 2))
                b28 = np.multiply(1 - np.power(b27, 2), np.exp(-np.power(b27, 2) / 2))
            elif self.b7 = = 2:
                b15 = np.power(b27, 3)
                b28 = 3 * np.power(b27, 2)
            else:
                b15 = np.tanh(b27)
                b28 = 1 - np.power(np.tanh(b27), 2)
            b29 = np.matmul(b15, b17.T.conj()) / b22
            b30 = np.multiply(b28.mean(axis=1).reshape(-1, 1), b24)
            b24 = b29 - b30
            b24 = self.fonk6(b24)
            u, s, b13 = np.linalg.svd(b24, compute_uv=True)
            b31 = np.diag(np.reciprocal(s))
            b32 = np.matmul(u, b31)
            b33 = np.matmul(u.T.conj(), b24)
            b24 = np.matmul(b32, b33)
            b25 = np.max(1 - np.abs(np.sum(np.multiply(b24, b26).conj(), axis=1)))
        print("Residual b34 = ", b25)
        b35 = fractional_matrix_power(np.diag(self.b5), 0.5)
        self.b6 = np.matmul(np.matmul(self.b4, b35), b24)
        return self.b6
    def fonk8(self):
        '''
        Compute the time coefficients or independent components of each mode
        '''
        b36 = self.fonk3(self.b1)
        b37 = np.array(self.b6.T.conj())
        b38 = np.array(b36.T.conj())
        b39 = np.matmul(b37, b38)
        return b39
    def fonk9(self):
        '''
        Plot the frequency transform of time coefficients of modes
        '''
        b40 = self.fonk8()
        a4 = 700
        b41 = 2 ** 13
        b42 = []
        for i in range(5):
            freq, b43 = welch(b40[i, :], nperseg=b41, nfft=b41, noverlap=b41 / 2, b52=a4)
            b42.append(b43)
        b42 = np.array(b42)
        b44 = []
        for i in range(5):
            b44.append('Mode %i' % (i + 1))
        fig, b45 = plt.subplots()
        for i in range(5):
            b45.plot(freq, b42[i, :], b46 = b44[i])
            b45.set_xlim(0, 10)
            b45.set_xlabel('Frequency (Hz)')
            b45.set_ylabel('Spectral Density (1/Hz)')
            b45.legend(b47 = 'best')
    def fonk10(self):
        '''
        Execute PCA and return PCA modes and their corresponding eigenvalues
        '''
        b10 = self.fonk3(self.b1)
        b48 = self.fonk5(b10)
        self.fonk7(b48)
    def fonk11(self):
        '''
        Visualize PCA modes
        '''
        self.fonk2(Plot_press)
        for i in range(self.b2):
            self.b3['id'](self.b6[:, i], ['red', 'white', 'blue'], b49 = True, num=i + 1)
        self.fonk9()
class class3(class1):
    def fonk12(self, b1, b2, b7, b50, b51, sampling_freq):
        class1.fonk12(self, b1, b2, b7)
        self.b50 = b50
        self.b51 = b51
        self.b52 = sampling_freq
        self.b53 = []
    def fonk13(self, signal):
        '''
        Remove frequencies outside the specified bandpass range
        '''
        b54 = len(signal)
        b55 = self.b52 / b54
        b56 = np.linspace(start=-self.b52 / 2, stop=self.b52 / 2 - b55, num=self.b1.shape[0]).T
        b57 = ((self.b50 < abs(b56)) & (abs(b56) < self.b51)).reshape(-1, 1)
        b58 = np.fft.fft(signal, axis=0)
        b59 = np.fft.fftshift(b58) / b54
        b60 = np.multiply(b57.astype(np.int), b59)
        b61 = np.fft.ifftshift(b60)
        b62 = np.fft.ifft(b61, axis=0)
        b63 = np.real(b62)
        return b63
    def fonk14(self, signal):
        '''
        Generate analytic signal using Hilbert transform to remove negative frequencies
        '''
        b64 = hilbert(signal, axis=0)
        return b64
    def fonk15(self):
        '''
        Execute Dynamic class1
        '''
        b65 = self.fonk3(self.b1)
        b66 = self.fonk13(b65)
        b67 = self.fonk14(b66)
        b68 = self.fonk5(b67)
        self.b53 = self.fonk7(b68)
    def fonk16(self, mode_no):
        '''
        Visualize the animated movie of PCA mode
        '''
        b69 = self.b53[:, mode_no]
        b70 = b69.reshape(-1, 1)
        b71 = np.exp(1j * np.linspace(0, 2 * np.pi, 100)).reshape(1, -1)
        b72 = np.real(b70 * b71)
        self.fonk2(Plot_press)
        plt.ion()
        for i in range(100):
            b73 = b72[:, i]
            self.b3['id'](b73, ['red', 'white', 'blue'], b49 = False, num=1)
            plt.pause(0.1)
            plt.clf()