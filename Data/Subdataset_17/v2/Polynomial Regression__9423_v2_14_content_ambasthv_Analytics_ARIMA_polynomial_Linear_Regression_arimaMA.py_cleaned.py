import numpy as np
import lmfit as lm
import itertools
class MACoeffEstimator:
    def __init__(self, y, acf, q, index):
        self.index = index
        self.q = q
        self.y = y
        self.acf = acf
    def fitter_fn(self, params, x1, x2, x3, data):
        a = params['a']
        b = params['b']
        k = params['k']
        model = [k * k for k in x1] + [a * i for i in x2] + [b * i for i in x3]
        return [k1 - k2 for k1, k2 in zip(model, data)]
    def get_thetas(self, y, et):
        x1 = et
        x2 = et[1:]
        x3 = et[2:]
        params = lm.Parameters()
        params.add('a', value=0, min=-1, max=1)
        params.add('b', value=0, min=-1, max=1)
        params.add('k', value=0, min=-1, max=1)
        result = lm.minimize(self.fitter_fn, params, args=(x1, x2, x3, y))
        return [result.params['a'].value, result.params['b'].value, result.params['k'].value]
    def prelim_thetas(self, acf, q):
        p = []
        prelim_theta = []
        theta = []
        p.append([1 - acf[1], 1, -acf[1]])
        x1arr = np.roots(p[0]).tolist()
        eliminations = [i for i in x1arr if isinstance(i, complex) or i > 1 or i < -1]
        theta.append([x for x in x1arr if x not in eliminations])
        if q == 2:
            x2arr = []
            for k in theta[0]:
                p = [acf[1] + acf[2], 1 - 2 * k, acf[1] + acf[2] + (acf[1] + acf[2]) * k ** 2 + k]
                x2arr = np.roots(p).tolist()
                eliminations = [i for i in x2arr if isinstance(i, complex) or i > 1 or i < -1]
            theta.append([x for x in x2arr if x not in eliminations])
        else:
            print("q>2 not supported")
        if len(theta) > 1:
            prelim_theta = list(itertools.product(*theta))
        else:
            prelim_theta = theta[0]
        return prelim_theta
    def get_ma_coeff(self):
        prelim_theta = self.prelim_thetas(self.acf, self.q)
        if len(self.y) < 10:
            print("Input time series not suitable for forecasting")
            return []
        et = []
        for theta in prelim_theta:
            if isinstance(theta, float):
                et.append([0, self.y[0], self.y[1] + theta * self.y[0]])
            else:
                et.append([0, self.y[0], self.y[1] + theta[0] * self.y[0],
                           self.y[2] + theta[1] * self.y[1] + theta[1] * theta[0] * self.y[0]])
        final_thetas = [self.get_thetas(self.y, e) for e in et]
        if self.index >= len(final_thetas):
            self.index = 0
        return final_thetas[self.index][:self.q]
y = [1, 2, 3, 4, 5]
acf = [1, 0.5, 0.2]
q = 2
index = 0
estimator = MACoeffEstimator(y, acf, q, index)
ma_coeffs = estimator.get_ma_coeff()
print(ma_coeffs)