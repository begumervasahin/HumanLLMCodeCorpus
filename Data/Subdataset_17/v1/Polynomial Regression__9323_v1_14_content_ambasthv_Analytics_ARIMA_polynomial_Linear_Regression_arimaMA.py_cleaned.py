import numpy as np
import lmfit as lm
import itertools
class MA_Coeff_Estimator:
    def __init__(self, y, acf, q, index):
        self.index = index
        self.q = q
        self.y = y
        self.acf = acf
    def fitterfn(self, params, x1, x2, x3, data):
        a = params['a']
        b = params['b']
        k = params['k']
        model = [k * k for k in x1] + [a * i for i in x2] + [b * i for i in x3]
        return [k1 - k2 for (k1, k2) in zip(model, data)]
    def getthetas(self, y, et):
        x1 = et
        x2 = et[1:]
        x3 = et[2:]
        finalthetas = []
        params = lm.Parameters()
        params.add('a', value=0, min=-1, max=1)
        params.add('b', value=0, min=-1, max=1)
        params.add('k', value=0, min=-1, max=1)
        result = lm.minimize(self.fitterfn, params, args=(x1, x2, x3, y))
        finalthetas.append(result.params.get('a').value)
        finalthetas.append(result.params.get('b').value)
        finalthetas.append(result.params.get('k').value)
        return finalthetas
    def prelimthetas(self, acf, q):
        p = []
        prelimtheta = []
        theta = []
        p.append([1 - acf[1], 1, -acf[1]])
        eliminations = []
        x1arr = np.roots(p[0]).tolist()
        for i in x1arr:
            if not isinstance(i, complex):
                if i > 1 or i < -1:
                    eliminations.append(i)
            else:
                eliminations.append(i)
        theta.append([x for x in x1arr if x not in eliminations])
        if q == 2:
            eliminations = []
            x2arr = []
            for k in theta[0]:
                p.append([acf[1] + acf[2], 1 - 2 * k, acf[1] + acf[2] + (acf[1] + acf[2]) * k ** 2 + k])
                x2arr = np.roots(p.pop()).tolist()
                for i in x2arr:
                    if not isinstance(i, complex):
                        if i > 1 or i < -1:
                            eliminations.append(i)
                    else:
                        eliminations.append(i)
            theta.append([x for x in x2arr if x not in eliminations])
        else:
            print("q>2 not supported")
        if len(theta) > 1:
            prelimtheta = list(itertools.product(*theta))
        else:
            prelimtheta = theta[0]
        return prelimtheta
    def getMaCoeff(self):
        prelimtheta = self.prelimthetas(self.acf, self.q)
        et = []
        if len(self.y) < 10:
            print("Input time series not suitable for forecasting")
            return
        for k in range(len(prelimtheta)):
            if isinstance(prelimtheta[k], float):
                list1 = [0, self.y[0], self.y[1] + prelimtheta[k] * self.y[0]]
            else:
                list1 = [0, self.y[0], self.y[1] + prelimtheta[k][0] * self.y[0],
                         self.y[2] + prelimtheta[k][1] * self.y[1] + prelimtheta[k][1] * prelimtheta[k][0] * self.y[0]]
            et.append(list1)
        finalthetas = []
        for k in range(len(et)):
            finalthetas.append(self.getthetas(self.y, et[k]))
        if self.index > len(finalthetas):
            self.index = 0
        return finalthetas[self.index][0:self.q]
y = [1, 2, 3, 4, 5]
acf = [1, 0.5, 0.2]
q = 2
index = 0
estimator = MA_Coeff_Estimator(y, acf, q, index)
ma_coeffs = estimator.getMaCoeff()
print(ma_coeffs)