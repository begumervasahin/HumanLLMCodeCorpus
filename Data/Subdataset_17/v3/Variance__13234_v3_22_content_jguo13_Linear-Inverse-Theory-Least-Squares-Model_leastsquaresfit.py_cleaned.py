import numpy as np
import matplotlib.pyplot as plt
class LeastSquares:
    def __init__(self, datafile):
        self.x, self.y, self.sigma = np.loadtxt(datafile, unpack=True)
    def expectation(self, nsteps, min_val, max_val):
        a_values = np.linspace(min_val, max_val, num=nsteps)
        b_values = np.linspace(min_val, max_val, num=nsteps)
        da = abs(max_val - min_val) / nsteps
        db = abs(max_val - min_val) / nsteps
        self.expa = 0
        self.expb = 0
        self.prob = np.zeros((nsteps, nsteps))
        for i in range(nsteps):
            for j in range(nsteps):
                self.prob[i, j] = self._calculate_probability(a_values[i], b_values[j])
        vol = np.sum(self.prob) * da * db
        self.vol = vol
        self._calculate_expectations(a_values, b_values, da, db)
        self.siga = np.sqrt(np.sum((a_values[:, None] - self.expa) ** 2 * self.prob * da * db / self.vol))
        self.sigb = np.sqrt(np.sum((b_values[None, :] - self.expb) ** 2 * self.prob * da * db / self.vol))
        self.covab = np.sum((a_values[:, None] - self.expa) * (b_values[None, :] - self.expb) * self.prob * da * db / self.vol)
        self.pco = self.covab / (self.siga * self.sigb)
    def _calculate_probability(self, a, b):
        prob_fxn = 1
        for k in range(len(self.x)):
            prob_fxn *= (1 / (np.sqrt(2 * np.pi) * self.sigma[k])) * \
                        np.exp(-((self.y[k] - (a * self.x[k] + b)) ** 2) / (2 * self.sigma[k] ** 2))
        return prob_fxn
    def _calculate_expectations(self, a_values, b_values, da, db):
        for i in range(len(a_values)):
            for j in range(len(b_values)):
                self.expa += a_values[i] * self.prob[i, j] * db * da / self.vol
                self.expb += b_values[j] * self.prob[i, j] * db * da / self.vol
    def plot_model(self):
        plt.plot(self.x, self.y, 'o', label='Data')
        xvar = np.linspace(0, 10, 100)
        model = self.expa * xvar + self.expb
        plt.plot(xvar, model, label='Model')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.legend()
        plt.show()
