import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import hilbert, welch
from visual import Plot_press
class PCA:
    def __init__(self, sample, num_modes):
        self.sample = sample
        self.num_modes = num_modes
        self.func_dict = {}
        self.func_add(lambda x: x)
        self.PCA_modes = []
        self.PCA_eigenvalues = []
    def func_add(self, func):
        '''Add a function to the class.'''
        self.func_dict['id'] = func
    def pre_process(self, signal):
        '''Remove the mean component from the sample and return the fluctuation component.'''
        signal_mean = np.mean(signal, axis=0).reshape(1, -1)
        signal_proc = signal - np.dot(np.ones((signal.shape[0], 1)), signal_mean)
        return signal_proc
    def calculate_covariance(self, signal):
        '''Return the covariance of the preprocessed sample.'''
        signal_proc = self.pre_process(signal)
        L = len(signal_proc)
        signal_cov = np.dot(signal_proc.T.conj(), signal_proc) / L
        return signal_cov
    def calculate_pca_modes(self, signal):
        '''Return PCA modes using singular value decomposition.'''
        signal_cov = self.calculate_covariance(signal)
        u, s, vh = np.linalg.svd(signal_cov, full_matrices=True)
        self.PCA_modes = u[:, :self.num_modes]
        self.PCA_eigenvalues = s[:self.num_modes]
    def calculate_principal_components(self):
        '''Compute the principal components of each mode.'''
        preprocessed_sample = self.pre_process(self.sample)
        principal_components = np.dot(self.PCA_modes.T, preprocessed_sample.T)
        return principal_components
    def plot_psd_pc(self):
        '''Plot the frequency transform of the time coefficients of the modes.'''
        principal_components = self.calculate_principal_components()
        sampling_frequency = 700
        nfft = 2 ** 13
        spec_array = []
        for i in range(self.num_modes):
            freq, spec = welch(principal_components[i, :], nperseg=nfft, nfft=nfft, noverlap=nfft
                               fs=sampling_frequency)
            spec_array.append(spec)
        spec_array = np.array(spec_array)
        fig, ax = plt.subplots()
        for i in range(self.num_modes):
            ax.plot(freq, spec_array[i, :], label=f'Mode {i + 1}')
        ax.set_xlim(0, 10)
        ax.set_xlabel('Frequency (Hz)')
        ax.set_ylabel('Spectral Density (1/Hz)')
        ax.legend(loc='best')
        plt.show()
    def execute_pca(self):
        '''Execute PCA and return PCA modes and their corresponding eigenvalues.'''
        self.calculate_pca_modes(self.sample)
        return self.PCA_modes, self.PCA_eigenvalues
    def visualize_pca_modes(self):
        '''Visualize PCA modes.'''
        self.func_add(Plot_press)
        for i in range(self.num_modes):
            self.func_dict['id'](self.PCA_modes[:, i], ['red', 'white', 'blue'], txt=True, num=i + 1)
        self.plot_psd_pc()
class DynamicPCA(PCA):
    def __init__(self, sample, num_modes, f1, f2, sampling_freq):
        super().__init__(sample, num_modes)
        self.f1 = f1
        self.f2 = f2
        self.sampling_freq = sampling_freq
        self.dynamic_pca_modes = []
        self.dynamic_pca_eigenvalues = []
    def bandpass_filter(self, signal):
        '''Remove frequencies that lie outside the range of the bandpass.'''
        signal_preprocessed = self.pre_process(signal)
        n = len(signal_preprocessed)
        dF = self.sampling_freq / n
        f = np.linspace(start=-self.sampling_freq / 2, stop=self.sampling_freq / 2 - dF, num=self.sample.shape[0]).T
        boolean_mask = ((self.f1 < abs(f)) & (abs(f) < self.f2)).reshape(-1, 1)
        fft_signal = np.fft.fft(signal_preprocessed, axis=0)
        fft_shifted = np.fft.fftshift(fft_signal) / n
        filtered_signal = np.fft.ifftshift(np.multiply(boolean_mask.astype(np.int), fft_shifted), axis=0)
        inverse_fft = np.fft.ifft(filtered_signal, axis=0)
        return np.real(inverse_fft)
    def hilbert_transform(self, signal):
        '''Create an analytic signal using the Hilbert transform.'''
        filtered_signal = self.bandpass_filter(signal)
        analytic_signal = hilbert(filtered_signal, axis=0)
        return analytic_signal
    def calculate_dynamic_pca_modes(self, signal):
        '''Return DynamicPCA modes.'''
        analytic_signal = self.hilbert_transform(signal)
        signal_cov = self.calculate_covariance(analytic_signal)
        u, s, vh = np.linalg.svd(np.array(signal_cov))
        self.dynamic_pca_modes = u[:, :self.num_modes]
        self.dynamic_pca_eigenvalues = s[:self.num_modes]
    def execute(self):
        '''Execute PCA and return PCA modes and their corresponding eigenvalues.'''
        self.calculate_dynamic_pca_modes(self.sample)
        return self.dynamic_pca_modes, self.dynamic_pca_eigenvalues
    def visualize(self, mode_no):
        '''Visualize the animated movie of PCA mode.'''
        dynamic_pca_mode = self.dynamic_pca_modes[:, mode_no]
        Z = dynamic_pca_mode.reshape(-1, 1)
        phase_shift = np.exp(1j * np.linspace(0, 2 * np.pi, 100)).reshape(1, -1)
        ZZ = np.real(Z * phase_shift)
        self.func_add(Plot_press)
        plt.ion()
        for i in range(100):
            press = ZZ[:, i]
            self.func_dict['id'](press, ['red', 'white', 'blue'], txt=False, num=1)
            plt.pause(0.1)
            plt.clf()
if __name__ == "__main__":
    sample_data = np.random.rand(100, 10)
    pca = PCA(sample_data, 3)
    pca.execute_pca()
    pca.visualize_pca_modes()